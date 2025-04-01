## Retrieval and Question Answering Exercise

In this exercise, your goal is to utilize a vector database to attempt to retrieve relevant context to answer questions about Best Picture winners since 2000. Each question can be answered from the Wikipedia page of each movie. 

You have been provided a list of movies and links to their Wikipedia pages in the file best_picture_2000.csv.

Build a vector database off of these Wikipedia pages which, given a query, can find potentially relevant context to answer the question. 

Then use a question-answering model from HugingFace to anwser the question.

A list of question and answer pairs is given in QAs.csv, but feel free to add to it yourself.

## Questions and Answers

| Film | Question | Answer | Generated Answer |
|------|----------|--------|------------------|
| Gladiator | What was the worldwide gross of Gladiator? | $465.4 million | $465.5 million |
| A Beautiful Mind | Who was consulted on the mathematical equations in the film A Beautiful Mind? | Dave Bayer | Dave Bayer |
| Chicago | Where did principal photography take place for the film Chicago? | Toronto, Ontario, Canada. | New Orleans, Louisiana |
| The Lord of the Rings: The Return of the King | Who composed the score for the film The Lord of the Rings: The Return of the King? | Howard Shore | Peter Jackson |
| Million Dollar Baby | What day was Million Dollar Baby released in theaters? | December 15, 2004 | December 15, 2004 |
| Crash | When was Crash released on DVD? | September 6, 2005 | September 6, 2005 |
| The Departed | How much did The Departed gross on opening weekend? | $26.9 million | $34.8 million |
| No Country for Old Men | The film No Country for Old Men is based on the novel by what author? | Cormac McCarthy | Cormac McCarthy |
| Slumdog Millionaire | Slumdog Millionaire is based on what novel? | Q & A | Q & A |
| The Hurt Locker | Where was The Hurt Locker filmed? | Jordan | 3rd Zurich Film Festival |
| The King's Speech | How many Oscar nominations did The King's Speech receive? | 12 | 12 |
| The Artist | Who directed The Artist? | Michel Hazanavicius | Michel Hazanavicius |
| Argo | When was Argo released in the United States? | October 12, 2012 | 2012 |
| 12 Years a Slave | 12 Years a Slave is based on whose memoir? | Solomon Northup | Solomon Northup |
| Birdman or (The Unexpected Virtue of Ignorance) | Where was Birdman filmed? | New York City | a theatre |
| Spotlight | How many Academy Award nominations did Spotlight receive? | six | six |
| Moonlight | Who composed the score for Moonlight? | Nicholas Britell | Nicholas Britell |
| The Shape of Water | Who directed The Shape of Water? | Guillermo del Toro | Guillermo del Toro |
| Green Book | What was the total worldwide gross of Green Book? | $321.8 million | $321.8 million |
| Parasite | What prize did Parasite win at the Cannes Film Festival? | Palme d'Or | Palme d'Or |
| Nomadland | What was the budget of Nomadland? | $5 million | $39.1 million |
| CODA | CODA is a remake of what film? | La Famille Bélier | La Famille Bélier |
| Everything Everywhere All at Once | Who stars as Evelyn Quan Wang in Everything Everywhere All at Once? | Michelle Yeoh | Michelle Yeoh |
| Oppenheimer | Where did Oppenheimer premiere? | Le Grand Rex in Paris | Le Grand Rex in Paris |


## Evaluation

The model gets most of the answers correct. 
