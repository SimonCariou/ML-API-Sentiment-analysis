import requests

def test_get_root_result():
    response = requests.get(
        url='http://127.0.0.1:8000/'
    )
    assert response.status_code == 200
    assert response.json() == {"Status":"The API is running"}