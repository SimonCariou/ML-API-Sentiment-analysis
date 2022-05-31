from fastapi import FastAPI, HTTPException, Request, status, Depends
from fastapi.responses import JSONResponse

from app.auth.auth_rules import get_auth_status, get_admin_auth_status
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
    description="Gives a score to a text review. The score ranges from 1 to 5; 1 being the most negative.",
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

def predict_sentence_rating(model, sentence):
    """ This function calculates the rating of a given sentence based on the specified model. The rating ranges from 1 to 5 where 1 corresponds to a negative sentence and 5 is a positive one.
    Input: Machine learning trained model (logistic regression, multinomialNB...)and the sentence (string) which we want to calculate the rating.
    Output: The rating calculated by the provided model
    """
    preprocessed_sentence = finalize_preprocess(sentence)
    transformed_sentence = tfidf_vectorizer.transform([preprocessed_sentence])
    return {
        "Sentence": sentence,
        "Ratings": model.predict(transformed_sentence)[0].tolist()
    }



""" API IMPLEMENTATION
"""

@api.get("/", responses=responses, name="Check if the API is running")
async def get_root():
    return {"Status": "The API is running"}


#GET the rating of a given sentence via 5 different ML models.
@api.get("/ratings/logistic_regression", responses=responses, name="Get the rating of a sentence calculated by the logistic regression model.")
async def get_logreg_ratin(sentence: str, isAuthenticated: bool = Depends(get_auth_status)):
    return predict_sentence_rating(log_reg_model, sentence)

@api.get("/ratings/decision_tree_classifier", responses=responses, name="Get the rating of a sentence calculated by the decision tree classifier model.")
async def get_dec_tree_rating(sentence: str, isAuthenticated: bool = Depends(get_auth_status)):
    return predict_sentence_rating(dec_tree_model, sentence)

@api.get("/ratings/multinomial_nb", responses=responses, name="Get the rating of a sentence calculated by the Multinomial Naive Bayes model.")
async def get_multinomial_nb_rating(sentence: str, isAuthenticated: bool = Depends(get_auth_status)):
    return predict_sentence_rating(multi_nb_model, sentence)

@api.get("/ratings/sgd_classifier", responses=responses, name="Get the rating of a sentence calculated by the Stochastic Gradient model.")
async def get_sgdc_rating(sentence: str, isAuthenticated: bool = Depends(get_auth_status)):
    return predict_sentence_rating(sgdc_model, sentence)



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