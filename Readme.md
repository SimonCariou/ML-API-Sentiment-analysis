# Description

## Presentation

This API is the second part of the Data Engineer machine learning project.
The first project being the training of several machine learning algorithms on train sets. 
We chose to train a sentiments algorithm on reviews from dating apps users on app stores.

## Goal

The goal is to write an API that:
- allows an authenticated user to send sentences and get the sentiment as a response: 0 if negative and 1 if positive. The sentiment can be calculated by different models, all accessible via their own endpoints:\
  (decision tree, logistic regression, SGD CLassifier & Multinomial NB), test it, contenerize it with docker and deploy it using a Kubernetes Ingress.
- allows an authenticated user to access the performances of the different models in order to chose the right one. The performances that the API will return are\
  the recall_score, the accuracy_score, the f1_score and the precision_score. 

## How to use it 

Available routes:
GET: + parameter: `{"sentence": "xxxx"}` and returns the sentiments of the given sentence according to the chosen model.
```
/sentiment/logistic_regression
/sentiment/decision_tree_classifier
/sentiment/multinomial_nb
/sentiment/sgd_classifier
```

GET: Returns the accuracy_score, f1_score, recall_score & precision_score for the chosen model
```
/performances/logistic_regression
/performances/decision_tree_classifier
/performances/multinomial_nb
/performances/sgd_classifier
```