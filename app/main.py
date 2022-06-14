from fastapi import FastAPI, HTTPException, Request, status, Depends
from fastapi.responses import JSONResponse

from app.auth.auth_rules import get_auth_status
import joblib
import os

from app.utils import finalize_preprocess
from app.constants import *

#from pydantic import BaseModel
#from typing import Optional, List

responses = {
    200: {"message": "OK"},
    404: {"message": "Item not found"},
    302: {"message": "The item was moved"},
    403: {"message": "Not enough privileges"}
}

api = FastAPI(
    title='ML API - Sentiment Analysis',
    description="Gives a sentiment to a text review. The sentiment is either 0 (negative sentence) or 1 (positive sentence)",
    version="1.0.0"
)

# Load the models
log_reg_model = joblib.load(os.path.join(MODELS_DIRECTORY, LOG_REG_FILENAME))
dec_tree_model = joblib.load(os.path.join(MODELS_DIRECTORY, DECISION_TREE_FILENAME))
multi_nb_model = joblib.load(os.path.join( MODELS_DIRECTORY, MULTINOMIAL_NAIVE_BAYES_FILENAME))
sgdc_model = joblib.load(os.path.join(MODELS_DIRECTORY, SGDC_FILENAME))

# Load the different models performances: metrics calculated on the test dataset
log_reg_performances = joblib.load(os.path.join(PERFORMANCES_DIRECTORY, LOG_REG_PERF_FILENAME))
dec_tree_performances = joblib.load(os.path.join(PERFORMANCES_DIRECTORY, DECISION_TREE_PERF_FILENAME))
multi_nb_performances = joblib.load(os.path.join( PERFORMANCES_DIRECTORY, MULTINOMIAL_NAIVE_BAYES_PERF_FILENAME))
sgdc_performances = joblib.load(os.path.join(PERFORMANCES_DIRECTORY, SGDC_PERF_FILENAME))

# Load the vectorizer
tfidf_vectorizer = joblib.load(os.path.join(MODELS_DIRECTORY, TFIDF_VECTORIZER_FILEMANE))

def predict_sentence_sentiment(model, sentence):
    """ This function calculates the sentiment of a given sentence based on the specified model. The sentiment is either 0 or 1 depending on if the sentence is estimated, respectively, negative or positive.
    Input: Machine learning trained model (logistic regression, multinomialNB...)and the sentence (string) which we want to calculate the sentiment.
    Output: The sentiment calculated by the provided model
    """
    preprocessed_sentence = finalize_preprocess(sentence)
    transformed_sentence = tfidf_vectorizer.transform([preprocessed_sentence])
    return {
        "sentence": sentence,
        "sentiment": model.predict(transformed_sentence)[0].tolist()
    }



""" API IMPLEMENTATION
"""

@api.get("/", responses=responses, name="Check if the API is running")
async def get_root():
    return {"Status": "The API is running"}


#GET the sentiment of a given sentence via 5 different ML models.
@api.get("/sentiment/logistic_regression", responses=responses, name="Get the sentiment (Positive: 1 or Negative: 0) of a sentence calculated by the logistic regression model.")
async def get_logreg_ratin(sentence: str, isAuthenticated: bool = Depends(get_auth_status)):
    return predict_sentence_sentiment(log_reg_model, sentence)

@api.get("/sentiment/decision_tree_classifier", responses=responses, name="Get the sentiment (Positive: 1 or Negative: 0) of a sentence calculated by the decision tree classifier model.")
async def get_dec_tree_sentiment(sentence: str, isAuthenticated: bool = Depends(get_auth_status)):
    return predict_sentence_sentiment(dec_tree_model, sentence)

@api.get("/sentiment/multinomial_nb", responses=responses, name="Get the sentiment (Positive: 1 or Negative: 0) of a sentence calculated by the Multinomial Naive Bayes model.")
async def get_multinomial_nb_sentiment(sentence: str, isAuthenticated: bool = Depends(get_auth_status)):
    return predict_sentence_sentiment(multi_nb_model, sentence)

@api.get("/sentiment/sgd_classifier", responses=responses, name="Get the sentiment (Positive: 1 or Negative: 0) of a sentence calculated by the Stochastic Gradient model.")
async def get_sgdc_sentiment(sentence: str, isAuthenticated: bool = Depends(get_auth_status)):
    return predict_sentence_sentiment(sgdc_model, sentence)


#GET the performances of the different models
@api.get("/performances/logistic_regression", responses=responses, name="Get the performances of the logistic regression model on the trained dataset.")
async def get_logreg_performances(isAuthenticated: bool = Depends(get_auth_status)):
    return log_reg_performances

@api.get("/performances/decision_tree_classifier", responses=responses, name="Get the performances of the decision tree classifier model on the trained dataset.")
async def get_dec_tree_performances(isAuthenticated: bool = Depends(get_auth_status)):
    return dec_tree_performances

@api.get("/performances/multinomial_nb", responses=responses, name="Get the performances of the Multinomial Naive Bayes model on the trained dataset.")
async def get_multinomial_nb_performances(isAuthenticated: bool = Depends(get_auth_status)):
    return multi_nb_performances

@api.get("/performances/sgd_classifier", responses=responses, name="Get the performances of the Stochastic Gradient classifier model on the trained dataset.")
async def get_sgdc_performances(isAuthenticated: bool = Depends(get_auth_status)):
    return sgdc_performances