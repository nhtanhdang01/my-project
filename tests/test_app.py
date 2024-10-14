# test_app.py
import pytest
from app import app  # Adjust the import based on your app's structure

def test_app():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
# test_app.py
import pytest
from app import app  # Adjust the import based on your app's structure

def test_app():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
