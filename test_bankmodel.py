import pytest
from flask_api import app

@pytest.fixture
def client():
    return app.test_client() 
def test_greet(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'Hello world'  
    #assert response.data == b'Hello world, welcome'  

def test_get_input(client):     
    response = client.get('/input')
    assert response.status_code == 200
    assert response.data == b'please provide input'

def test_predict(client):
    data = {
        "variance": 0.1,
        "skewness": 0.2,
        "curtosis": 0.3,
        "entropy": 0.4
    }
    response = client.post('/predict', json=data)
    assert response.status_code == 200
    response_data = response.get_json()
    assert "The Currency Note is " in response_data
    assert response_data["The Currency Note is "] in ["Authorised", "Unauthorised"] 
