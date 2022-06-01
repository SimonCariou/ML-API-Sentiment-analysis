import requests
from requests.auth import HTTPBasicAuth
from utils import check_metrics_value_range, check_metrics_list_returned

test_user = {
        'username': 'bob',
        'password': 'builder',
}

performances_metrics_measured = ["accuracy_score", "f1_score", "recall_score", "precision_score"]

def test_get_performances_logistic_regression_not_authenticated():
    """ Check that a non authenticated call is successfully cached
    """
    response = requests.get(
        url='http://127.0.0.1:8000/performances/logistic_regression'
    )
    assert response.status_code == 401
    assert response.json() == {"detail":"Not authenticated"}

#LOGISTIC REGRESSION
def test_get_performances_logistic_regression_wrong_authentication():
    response = requests.get(
        url='http://127.0.0.1:8000/performances/logistic_regression',
        auth = HTTPBasicAuth(test_user["username"], "wrong password")
        )
    assert response.status_code == 401
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_get_performances_logistic_regression_authenticated():
    response = requests.get(
        url='http://127.0.0.1:8000/performances/logistic_regression',
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    assert response.status_code == 200
    
def test_get_performances_logistic_regression_authenticated_range_metrics():
    response = requests.get(
        url='http://127.0.0.1:8000/performances/logistic_regression',
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    performances_list = [response.json()[metric] for metric in performances_metrics_measured]

    assert response.status_code == 200
    assert all(metric >= 0 and metric <=1 and metric != None and isinstance(metric, float) for metric in performances_list)

def test_check_returned_metrics_are_in_expected_list_of_metrics_logistic_regression():
    response = requests.get(
        url='http://127.0.0.1:8000/performances/logistic_regression',
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    
    response_keys = [key for key in response.json()]

    assert response.status_code == 200
    assert check_metrics_list_returned(response_keys)


#DECISION TREE CLASSIFIER
def test_get_performances_decision_tree_classifier_wrong_authentication():
    response = requests.get(
        url='http://127.0.0.1:8000/performances/decision_tree_classifier',
        auth = HTTPBasicAuth(test_user["username"], "wrong password")
        )
    assert response.status_code == 401
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_get_performances_decision_tree_classifier_authenticated():
    response = requests.get(
        url='http://127.0.0.1:8000/performances/decision_tree_classifier',
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    assert response.status_code == 200
    
def test_get_performances_decision_tree_classifier_authenticated_range_metrics():
    response = requests.get(
        url='http://127.0.0.1:8000/performances/decision_tree_classifier',
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    performances_list = [response.json()[metric] for metric in performances_metrics_measured]

    assert response.status_code == 200
    assert check_metrics_value_range(performances_list)

def test_check_returned_metrics_are_in_expected_list_of_metrics_decision_tree_classifier():
    response = requests.get(
        url='http://127.0.0.1:8000/performances/decision_tree_classifier',
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    
    response_keys = [key for key in response.json()]

    assert response.status_code == 200
    assert check_metrics_list_returned(response_keys)

#MULTINOMIAL_NB
def test_get_performances_multinomial_nb_wrong_authentication():
    response = requests.get(
        url='http://127.0.0.1:8000/performances/multinomial_nb',
        auth = HTTPBasicAuth(test_user["username"], "wrong password")
        )
    assert response.status_code == 401
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_get_performances_multinomial_nb_authenticated():
    response = requests.get(
        url='http://127.0.0.1:8000/performances/multinomial_nb',
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    assert response.status_code == 200
    
def test_get_performances_multinomial_nb_authenticated_range_metrics():
    response = requests.get(
        url='http://127.0.0.1:8000/performances/multinomial_nb',
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    performances_list = [response.json()[metric] for metric in performances_metrics_measured]

    assert response.status_code == 200
    assert check_metrics_value_range(performances_list)


def test_check_returned_metrics_are_in_expected_list_of_metrics_multinomial_nb():
    response = requests.get(
        url='http://127.0.0.1:8000/performances/multinomial_nb',
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    
    response_keys = [key for key in response.json()]

    assert response.status_code == 200
    assert check_metrics_list_returned(response_keys)

#STOCHASTIC GRADIENT CLASSIFIER
def test_get_performances_sgd_classifier_wrong_authentication():
    response = requests.get(
        url='http://127.0.0.1:8000/performances/sgd_classifier',
        auth = HTTPBasicAuth(test_user["username"], "wrong password")
        )
    assert response.status_code == 401
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_get_performances_sgd_classifier_authenticated():
    response = requests.get(
        url='http://127.0.0.1:8000/performances/sgd_classifier',
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    assert response.status_code == 200
    
def test_get_performances_sgd_classifier_authenticated_range_metrics():
    response = requests.get(
        url='http://127.0.0.1:8000/performances/sgd_classifier',
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    performances_list = [response.json()[metric] for metric in performances_metrics_measured]

    assert response.status_code == 200
    assert check_metrics_value_range(performances_list)

def test_check_returned_metrics_are_in_expected_list_of_metrics_sgd_classifier():
    response = requests.get(
        url='http://127.0.0.1:8000/performances/sgd_classifier',
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    
    response_keys = [key for key in response.json()]

    assert response.status_code == 200
    assert check_metrics_list_returned(response_keys)