import re
import requests

def test_get_performances_logistic_regressionf_not_authenticated():
    response = requests.get(
        url='http://127.0.0.1:8000/performances/logistic_regression'
    )
    assert response.status_code == 401
    assert response.json() == {"detail":"Not authenticated"}
