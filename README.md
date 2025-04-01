## Retrieval and Question Answering Exercise

In this exercise, your goal is to utilize a vector database to attempt to retrieve relevant context to answer questions about Best Picture winners since 2000. Each question can be answered from the Wikipedia page of each movie. 

You have been provided a list of movies and links to their Wikipedia pages in the file best_picture_2000.csv.

Build a vector database off of these Wikipedia pages which, given a query, can find potentially relevant context to answer the question. 

Then use a question-answering model from HugingFace to anwser the question.

A list of question and answer pairs is given in QAs.csv, but feel free to add to it yourself.