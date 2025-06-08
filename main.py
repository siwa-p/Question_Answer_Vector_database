import pandas as pd
from transformers import pipeline, set_seed
from sentence_transformers import SentenceTransformer
import requests
from bs4 import BeautifulSoup
import chromadb
from nltk.tokenize import sent_tokenize
from tqdm.notebook import tqdm
import numpy as np
import nltk
import os
import sys

current_path = os.getcwd()
nltk_data_path = f'{current_path}/nltk_data'
nltk.data.path.append(nltk_data_path)

if not os.path.exists(os.path.join(nltk_data_path, 'tokenizers', 'punkt')):
    nltk.download('punkt', download_dir=nltk_data_path)
    
# Function to scrape text from links
def get_text(link):
    response = requests.get(link)
    soup = BeautifulSoup(response.text)
    paragraphs = soup.find(id='mw-content-text').find_all('p')
    text = '\n'.join([p.get_text() for p in paragraphs])
    return text

def add_picture(picture):
    sentences = sent_tokenize(picture['body_text'])
    collection.add(
        documents = sentences,
        ids = [f'{picture["index"]}_{i}' for i in range(len(sentences))],
        metadatas = [{'picture': picture['title']}] * len(sentences)
    )

def add_data(picture_info):
    for _, row in tqdm(picture_info.iterrows()):
        print(row['title'])
        add_picture(row)


# Function to retrieve context based on a question
def context(question):
    results = collection.query(
        query_texts=[question],
        n_results=5
    )
    return '\n'.join(results['documents'][0])

# Generate answers
def answer_generation(row):
    question = row['question']
    context = row['context']  
    try:
        answer = qa(question=question, context=context)
        return answer['answer']
    except ValueError as e:
        print(f"Error generating answer for question '{question}': {e}")
        return "Error: Unable to generate answer"
    

if __name__ == '__main__':    
    # Load data
    picture_info = pd.read_csv('data/best_picture_2000.csv')
    # Add body text to the dataframe
    picture_info['body_text'] = picture_info['link'].apply(get_text)
    picture_info = picture_info.reset_index()

    client = chromadb.PersistentClient(path=f'{current_path}/chromadb')
    
    if "picture_info" not in [c.name for c in client.list_collections()]:
        collection = client.create_collection("picture_info")
    else:
        collection = client.get_collection("picture_info")
        
    # Load questions and add context
    questions = pd.read_csv(f'{current_path}/data/QAs.csv')
    questions['context'] = questions['question'].apply(context)

    # Initialize models
    encoder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    decoder = pipeline('text-generation', model='distilgpt2')
    qa = pipeline(task="question-answering")
    
    questions['answer_generated'] = questions.apply(answer_generation, axis=1)

    # Compare generated answers with actual answers
    questions[['question', 'answer', 'answer_generated']]
    accuracy = np.sum(questions['answer'] == questions['answer_generated'])
    print(f"Accuracy: {accuracy}")


    