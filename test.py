from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_homepage():
# Send a GET request to the root URL
    response = client.get ("/")
# Check if the response status is 200 0K
    assert response. status_code == 200
# Check if the HTML content returned contains a specific string
    assert "<title>Index - iPortfolio Bootstrap Template</title>" in response.text