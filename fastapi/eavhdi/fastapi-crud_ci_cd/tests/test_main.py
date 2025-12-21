from fastapi.testclient import TestClient
from main import app 

client = TestClient(app)

def test_create_item():
    response = client.post('/items', json="Apple")
    assert response.status_code == 200 