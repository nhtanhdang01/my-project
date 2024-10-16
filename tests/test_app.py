import pytest
from app.app import app  # Import the app instance correctly

@pytest.fixture
def client():
    app.config['TESTING'] = True  # Enable testing mode
    with app.test_client() as client:  # Create a test client
        yield client  # Yield the client to the test functions

def test_home(client):
    """Test the home page."""
    response = client.get('/')  # Make a GET request to the home page
    assert response.status_code == 200  # Check for 200 OK
