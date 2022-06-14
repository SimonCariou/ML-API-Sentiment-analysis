import requests
from requests.auth import HTTPBasicAuth
from utils import check_sentiment_in_response_are_int, check_sentiment_in_response_are_within_range, check_status_code_is_200_in_list_of_responses

test_user = {
        'username': 'bob',
        'password': 'builder',
}

sentences = {
                0: "The app is bad",
                1: "I like it very much"
    }


address = "127.0.0.1"
port = "8000"

def test_get_root_result():
    response = requests.get(
        url='http://{api_address}:{api_port}/'.format(api_address = address, api_port = port)
    )
    assert response.status_code == 200
    assert response.json() == {"Status":"The API is running"}

#LOGISTIC REGRESSION
def test_get_sentiment_logistic_regression_not_authenticated():
    """ Check that a non authenticated call is successfully caught
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/sentiment/logistic_regression'.format(api_address = address, api_port = port)
    )
    assert response.status_code == 401
    assert response.json() == {"detail":"Not authenticated"}

def test_get_sentiment_logistic_regression_wrong_authentication():
    """ Check that a wrong username/password combination is successfully caught
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/sentiment/logistic_regression'.format(api_address = address, api_port = port),
        auth = HTTPBasicAuth(test_user["username"], "wrong password")
        )
    assert response.status_code == 401
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_get_sentiment_logistic_regression_authenticated_no_parameters_given():
    """ Check that a call without the sencence as a parameter is successfully caught and thows an error 422
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/sentiment/logistic_regression'.format(api_address = address, api_port = port),
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    assert response.status_code == 422

def test_get_sentiment_logistic_regression_authenticated_are_valid():
    """ This test performs 2 requests, taking the sentences in the sentences dictionnary (defined at the top of the file), and  
    check that after performing well built requests, the responses meet the following criterias:
    - the status code of all of the requests is 200
    - the sentiment obtained in the responses are ints and are either 0 or 1
    """
    responses = [requests.get( 
            url = 'http://{api_address}:{api_port}/sentiment/logistic_regression'.format(api_address = address, api_port = port),
            auth = HTTPBasicAuth(test_user["username"], test_user["password"]),
            params = {"sentence": sentence}) \
                    for sentence in sentences.values()]
    assert check_status_code_is_200_in_list_of_responses(responses)
    assert check_sentiment_in_response_are_int(responses)
    assert check_sentiment_in_response_are_within_range(responses)  

#DECISION TREE CLASSIFIER
def test_get_sentiment_decision_tree_classifier_not_authenticated():
    """ Check that a non authenticated call is successfully caught
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/sentiment/decision_tree_classifier'.format(api_address = address, api_port = port)
    )
    assert response.status_code == 401
    assert response.json() == {"detail":"Not authenticated"}

def test_get_sentiment_decision_tree_classifier_wrong_authentication():
    """ Check that a wrong username/password combination is successfully caught
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/sentiment/decision_tree_classifier'.format(api_address = address, api_port = port),
        auth = HTTPBasicAuth(test_user["username"], "wrong password")
        )
    assert response.status_code == 401
    assert response.json() == {'detail': 'Incorrect email or password'}

def test_get_sentiment_decision_tree_classifier_authenticated_no_parameters_given():
    """ Check that a call without the sencence as a parameter is successfully caught and thows an error 422
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/sentiment/decision_tree_classifier'.format(api_address = address, api_port = port),
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    assert response.status_code == 422

def test_get_sentiment_decision_tree_classifier_authenticated_are_valid():
    """ This test performs 2 requests, taking the sentences in the sentences dictionnary (defined at the top of the file), and  
    check that after performing well built requests, the responses meet the following criterias:
    - the status code of all of the requests is 200
    - the sentiment obtained in the responses are ints and are either 0 or 1
    """
    responses = [requests.get( 
            url = 'http://{api_address}:{api_port}/sentiment/decision_tree_classifier'.format(api_address = address, api_port = port),
            auth = HTTPBasicAuth(test_user["username"], test_user["password"]),
            params = {"sentence": sentence}) \
                    for sentence in sentences.values()]
    assert check_status_code_is_200_in_list_of_responses(responses)
    assert check_sentiment_in_response_are_int(responses)
    assert check_sentiment_in_response_are_within_range(responses)  

#MULTINOMIAL_NB
def test_get_sentiment_multinomial_nb_not_authenticated():
    """ Check that a non authenticated call is successfully caught
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/sentiment/multinomial_nb'.format(api_address = address, api_port = port)
    )
    assert response.status_code == 401
    assert response.json() == {"detail":"Not authenticated"}

def test_get_sentiment_multinomial_nb_wrong_authentication():
    """ Check that a wrong username/password combination is successfully caught
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/sentiment/multinomial_nb'.format(api_address = address, api_port = port),
        auth = HTTPBasicAuth(test_user["username"], "wrong password")
        )
    assert response.status_code == 401
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_get_sentiment_multinomial_nb_authenticated_no_parameters_given():
    """ Check that a call without the sencence as a parameter is successfully caught and thows an error 422
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/sentiment/multinomial_nb'.format(api_address = address, api_port = port),
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    assert response.status_code == 422

def test_get_sentiment_multinomial_nb_authenticated_are_valid():
    """ This test performs 2 requests, taking the sentences in the sentences dictionnary (defined at the top of the file), and  
    check that after performing well built requests, the responses meet the following criterias:
    - the status code of all of the requests is 200
    - the sentiment obtained in the responses are ints and are either 0 or 1
    """
    responses = [requests.get( 
            url = 'http://{api_address}:{api_port}/sentiment/multinomial_nb'.format(api_address = address, api_port = port),
            auth = HTTPBasicAuth(test_user["username"], test_user["password"]),
            params = {"sentence": sentence}) \
                    for sentence in sentences.values()]
    assert check_status_code_is_200_in_list_of_responses(responses)
    assert check_sentiment_in_response_are_int(responses)
    assert check_sentiment_in_response_are_within_range(responses)  

#STOCHASTIC GRADIENT CLASSIFIER
def test_get_sentiment_sgd_classifier_not_authenticated():
    """ Check that a non authenticated call is successfully caught
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/sentiment/sgd_classifier'.format(api_address = address, api_port = port)
    )
    assert response.status_code == 401
    assert response.json() == {"detail":"Not authenticated"}

def test_get_sentiment_sgd_classifier_wrong_authentication():
    """ Check that a wrong username/password combination is successfully caught
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/sentiment/sgd_classifier'.format(api_address = address, api_port = port),
        auth = HTTPBasicAuth(test_user["username"], "wrong password")
        )
    assert response.status_code == 401
    assert response.json() == {'detail': 'Incorrect email or password'}

def test_get_sentiment_sgd_classifier_authenticated_no_parameters_given():
    """ Check that a call without the sencence as a parameter is successfully caught and thows an error 422
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/sentiment/sgd_classifier'.format(api_address = address, api_port = port),
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    assert response.status_code == 422

def test_get_sentiment_sgd_classifier_authenticated_are_valid():
    """ This test performs 2 requests, taking the sentences in the sentences dictionnary (defined at the top of the file), and  
    check that after performing well built requests, the responses meet the following criterias:
    - the status code of all of the requests is 200
    - the sentiment obtained in the responses are ints and are either 0 or 1
    """
    responses = [requests.get( 
            url = 'http://{api_address}:{api_port}/sentiment/sgd_classifier'.format(api_address = address, api_port = port),
            auth = HTTPBasicAuth(test_user["username"], test_user["password"]),
            params = {"sentence": sentence}) \
                    for sentence in sentences.values()]
    assert check_status_code_is_200_in_list_of_responses(responses)
    assert check_sentiment_in_response_are_int(responses)
    assert check_sentiment_in_response_are_within_range(responses)  