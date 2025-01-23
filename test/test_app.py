import pytest
from app.main import app

@pytest.fixture 
def client():
  app.testing = True 
  return app.test_client()

def test_home(client):
  response = client.get("/")
  assert response.status.code == 200;
  assert response.get_json() == {"message": "Hello World"}