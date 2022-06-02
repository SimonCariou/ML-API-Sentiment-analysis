import requests
from requests.auth import HTTPBasicAuth
from utils import check_metrics_value_range, check_metrics_list_returned

test_user = {
        'username': 'bob',
        'password': 'builder',
}

performances_metrics_measured = ["accuracy_score", "f1_score", "recall_score", "precision_score"]

address = "127.0.0.1"
port = "8001"

#LOGISTIC REGRESSION
def test_get_performances_logistic_regression_not_authenticated():
    """ Check that a non authenticated call is successfully caught
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/performances/logistic_regression'.format(api_address = address, api_port = port) 
    )
    assert response.status_code == 401
    assert response.json() == {"detail":"Not authenticated"}

def test_get_performances_logistic_regression_wrong_authentication():
    """ Check that a wrong username/password combination is successfully caught
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/performances/logistic_regression'.format(api_address = address, api_port = port),
        auth = HTTPBasicAuth(test_user["username"], "wrong password")
        )
    assert response.status_code == 401
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_get_performances_logistic_regression_authenticated():
    """ Check that an authenticated and valid request returns a status_code 200
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/performances/logistic_regression'.format(api_address = address, api_port = port),
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    assert response.status_code == 200
    
def test_check_returned_metrics_are_in_expected_list_of_metrics_logistic_regression():
    """ Check that the response is a json and that the keys (which are the metrics used to rate the model) are indeed in the
    list of expected metrics (performances_metrics_measured defined at the top of the file)
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/performances/logistic_regression'.format(api_address = address, api_port = port),
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    
    response_keys = [key for key in response.json()]

    assert response.status_code == 200
    assert check_metrics_list_returned(response_keys)

def test_get_performances_logistic_regression_authenticated_range_metrics():
    """ Check that the response is a json and that the values are indeed in within the range of expected results (between
    0 and 1 based on the way these are mathematically calculated)
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/performances/logistic_regression'.format(api_address = address, api_port = port),
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    performances_list = [response.json()[metric] for metric in performances_metrics_measured]

    assert response.status_code == 200
    assert check_metrics_value_range(performances_list)


#DECISION TREE CLASSIFIER
def test_get_performances_decision_tree_classifier_not_authenticated():
    """ Check that a non authenticated call is successfully caught
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/performances/decision_tree_classifier'.format(api_address = address, api_port = port)
    )
    assert response.status_code == 401
    assert response.json() == {"detail":"Not authenticated"}

def test_get_performances_decision_tree_classifier_wrong_authentication():
    """ Check that a wrong username/password combination is successfully caught
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/performances/decision_tree_classifier'.format(api_address = address, api_port = port),
        auth = HTTPBasicAuth(test_user["username"], "wrong password")
        )
    assert response.status_code == 401
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_get_performances_decision_tree_classifier_authenticated():
    """ Check that an authenticated and valid request returns a status_code 200
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/performances/decision_tree_classifier'.format(api_address = address, api_port = port),
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    assert response.status_code == 200

def test_check_returned_metrics_are_in_expected_list_of_metrics_decision_tree_classifier():
    """ Check that the response is a json and that the keys (which are the metrics used to rate the model) are indeed in the
    list of expected metrics (performances_metrics_measured defined at the top of the file)
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/performances/decision_tree_classifier'.format(api_address = address, api_port = port),
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    
    response_keys = [key for key in response.json()]

    assert response.status_code == 200
    assert check_metrics_list_returned(response_keys)

def test_get_performances_decision_tree_classifier_authenticated_range_metrics():
    """ Check that the response is a json and that the values are indeed in within the range of expected results (between
    0 and 1 based on the way these are mathematically calculated)
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/performances/decision_tree_classifier'.format(api_address = address, api_port = port),
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    performances_list = [response.json()[metric] for metric in performances_metrics_measured]

    assert response.status_code == 200
    assert check_metrics_value_range(performances_list)


#MULTINOMIAL_NB
def test_get_performances_multinomial_nb_not_authenticated():
    """ Check that a non authenticated call is successfully caught
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/performances/multinomial_nb'.format(api_address = address, api_port = port)
    )
    assert response.status_code == 401
    assert response.json() == {"detail":"Not authenticated"}

def test_get_performances_multinomial_nb_wrong_authentication():
    """ Check that a wrong username/password combination is successfully caught
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/performances/multinomial_nb'.format(api_address = address, api_port = port),
        auth = HTTPBasicAuth(test_user["username"], "wrong password")
        )
    assert response.status_code == 401
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_get_performances_multinomial_nb_authenticated():
    """ Check that an authenticated and valid request returns a status_code 200
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/performances/multinomial_nb'.format(api_address = address, api_port = port),
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    assert response.status_code == 200
    
def test_check_returned_metrics_are_in_expected_list_of_metrics_multinomial_nb():
    """ Check that the response is a json and that the keys (which are the metrics used to rate the model) are indeed in the
    list of expected metrics (performances_metrics_measured defined at the top of the file)
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/performances/multinomial_nb'.format(api_address = address, api_port = port),
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    
    response_keys = [key for key in response.json()]

    assert response.status_code == 200
    assert check_metrics_list_returned(response_keys)

def test_get_performances_multinomial_nb_authenticated_range_metrics():
    """ Check that the response is a json and that the values are indeed in within the range of expected results (between
    0 and 1 based on the way these are mathematically calculated)
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/performances/multinomial_nb'.format(api_address = address, api_port = port),
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    performances_list = [response.json()[metric] for metric in performances_metrics_measured]

    assert response.status_code == 200
    assert check_metrics_value_range(performances_list)

#STOCHASTIC GRADIENT CLASSIFIER
def test_get_performances_sgd_classifier_not_authenticated():
    """ Check that a non authenticated call is successfully caught
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/performances/sgd_classifier'.format(api_address = address, api_port = port)
    )
    assert response.status_code == 401
    assert response.json() == {"detail":"Not authenticated"}

def test_get_performances_sgd_classifier_wrong_authentication():
    """ Check that a wrong username/password combination is successfully caught
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/performances/sgd_classifier'.format(api_address = address, api_port = port),
        auth = HTTPBasicAuth(test_user["username"], "wrong password")
        )
    assert response.status_code == 401
    assert response.json() == {'detail': 'Incorrect email or password'}


def test_get_performances_sgd_classifier_authenticated():
    """ Check that an authenticated and valid request returns a status_code 200
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/performances/sgd_classifier'.format(api_address = address, api_port = port),
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    assert response.status_code == 200

def test_check_returned_metrics_are_in_expected_list_of_metrics_sgd_classifier():
    """ Check that the response is a json and that the keys (which are the metrics used to rate the model) are indeed in the
    list of expected metrics (performances_metrics_measured defined at the top of the file)
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/performances/sgd_classifier'.format(api_address = address, api_port = port),
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    
    response_keys = [key for key in response.json()]

    assert response.status_code == 200
    assert check_metrics_list_returned(response_keys)

def test_get_performances_sgd_classifier_authenticated_range_metrics():
    """ Check that the response is a json and that the values are indeed in within the range of expected results (between
    0 and 1 based on the way these are mathematically calculated)
    """
    response = requests.get(
        url='http://{api_address}:{api_port}/performances/sgd_classifier'.format(api_address = address, api_port = port),
        auth = HTTPBasicAuth(test_user["username"], test_user["password"])
        )
    performances_list = [response.json()[metric] for metric in performances_metrics_measured]

    assert response.status_code == 200
    assert check_metrics_value_range(performances_list)