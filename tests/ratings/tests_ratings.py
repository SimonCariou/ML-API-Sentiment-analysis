import requests
from requests.auth import HTTPBasicAuth
from utils import check_ratings_in_response_are_int, check_ratings_in_response_are_within_range, check_status_code_is_200_in_list_of_responses

test_user = {
        'username': 'bob',
        'password': 'builder',
}

sentences = {
                1: "The app is bad",
                2: "I guess it's fine",
                3: "This app is okay, but there are a ton of notifications that you can't see unless you pay",
                4: "Dope",
                5: "I like it very much"
    }


def test_get_root_result():
    response = requests.get(
        url='http://127.0.0.1:8000/'
    )
    assert response.status_code == 200
    assert response.json() == {"Status":"The API is running"}

#LOGISTIC REGRESSION
def test_get_ratings_logistic_regression_not_authenticated():
    """ Check that a non authenticated call is successfully caught
    """
    response = requests.get(
        url='http://127.0.0.1:8000/ratings/logistic_regression'
    )
    assert response.status_code == 401
    assert response.json() == {"detail":"Not authenticated"}

def test_get_ratings_logistic_regression_wrong_authentication():
    response = requests.get(
        url='http://127.0.0.1:8000/ratings/logistic_regression',
        auth = HTTPBasicAuth(test_user["username"], "wrong password")
        )
    assert response.status_code == 401
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_get_ratings_logistic_regression_authenticated_no_parameters_given():
    response = requests.get(
        url='http://127.0.0.1:8000/ratings/logistic_regression',
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    assert response.status_code == 422

def test_get_ratings_logistic_regression_authenticated_are_valid():
    responses = [requests.get( 
            url = 'http://127.0.0.1:8000/ratings/logistic_regression',
            auth = HTTPBasicAuth(test_user["username"], test_user["password"]),
            params = {"sentence": sentence}) \
                    for sentence in sentences.values()]
    assert check_status_code_is_200_in_list_of_responses(responses)
    assert check_ratings_in_response_are_int(responses)
    assert check_ratings_in_response_are_within_range(responses)  

#DECISION TREE CLASSIFIER
def test_get_ratings_decision_tree_classifier_not_authenticated():
    """ Check that a non authenticated call is successfully caught
    """
    response = requests.get(
        url='http://127.0.0.1:8000/ratings/decision_tree_classifier'
    )
    assert response.status_code == 401
    assert response.json() == {"detail":"Not authenticated"}

def test_get_ratings_decision_tree_classifier_wrong_authentication():
    response = requests.get(
        url='http://127.0.0.1:8000/ratings/decision_tree_classifier',
        auth = HTTPBasicAuth(test_user["username"], "wrong password")
        )
    assert response.status_code == 401
    assert response.json() == {'detail': 'Incorrect email or password'}

def test_get_ratings_decision_tree_classifier_authenticated_no_parameters_given():
    response = requests.get(
        url='http://127.0.0.1:8000/ratings/decision_tree_classifier',
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    assert response.status_code == 422

def test_get_ratings_decision_tree_classifier_authenticated_are_valid():
    responses = [requests.get( 
            url = 'http://127.0.0.1:8000/ratings/decision_tree_classifier',
            auth = HTTPBasicAuth(test_user["username"], test_user["password"]),
            params = {"sentence": sentence}) \
                    for sentence in sentences.values()]
    assert check_status_code_is_200_in_list_of_responses(responses)
    assert check_ratings_in_response_are_int(responses)
    assert check_ratings_in_response_are_within_range(responses)  

#MULTINOMIAL_NB
def test_get_ratings_multinomial_nb_not_authenticated():
    """ Check that a non authenticated call is successfully caught
    """
    response = requests.get(
        url='http://127.0.0.1:8000/ratings/multinomial_nb'
    )
    assert response.status_code == 401
    assert response.json() == {"detail":"Not authenticated"}

def test_get_ratings_multinomial_nb_wrong_authentication():
    response = requests.get(
        url='http://127.0.0.1:8000/ratings/multinomial_nb',
        auth = HTTPBasicAuth(test_user["username"], "wrong password")
        )
    assert response.status_code == 401
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_get_ratings_multinomial_nb_authenticated_no_parameters_given():
    response = requests.get(
        url='http://127.0.0.1:8000/ratings/multinomial_nb',
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    assert response.status_code == 422

def test_get_ratings_multinomial_nb_authenticated_are_valid():
    responses = [requests.get( 
            url = 'http://127.0.0.1:8000/ratings/multinomial_nb',
            auth = HTTPBasicAuth(test_user["username"], test_user["password"]),
            params = {"sentence": sentence}) \
                    for sentence in sentences.values()]
    assert check_status_code_is_200_in_list_of_responses(responses)
    assert check_ratings_in_response_are_int(responses)
    assert check_ratings_in_response_are_within_range(responses)  

#STOCHASTIC GRADIENT CLASSIFIER
def test_get_ratings_sgd_classifier_not_authenticated():
    """ Check that a non authenticated call is successfully caught
    """
    response = requests.get(
        url='http://127.0.0.1:8000/ratings/sgd_classifier'
    )
    assert response.status_code == 401
    assert response.json() == {"detail":"Not authenticated"}

def test_get_ratings_sgd_classifier_wrong_authentication():
    response = requests.get(
        url='http://127.0.0.1:8000/ratings/sgd_classifier',
        auth = HTTPBasicAuth(test_user["username"], "wrong password")
        )
    assert response.status_code == 401
    assert response.json() == {'detail': 'Incorrect email or password'}

def test_get_ratings_sgd_classifier_authenticated_no_parameters_given():
    response = requests.get(
        url='http://127.0.0.1:8000/ratings/sgd_classifier',
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    assert response.status_code == 422

def test_get_ratings_sgd_classifier_authenticated_are_valid():
    responses = [requests.get( 
            url = 'http://127.0.0.1:8000/ratings/sgd_classifier',
            auth = HTTPBasicAuth(test_user["username"], test_user["password"]),
            params = {"sentence": sentence}) \
                    for sentence in sentences.values()]
    assert check_status_code_is_200_in_list_of_responses(responses)
    assert check_ratings_in_response_are_int(responses)
    assert check_ratings_in_response_are_within_range(responses)  