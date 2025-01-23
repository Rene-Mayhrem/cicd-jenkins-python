import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import app

@pytest.fixture 
def client():
  app.testing = True 
  return app.test_client()

def test_home(client):
  response = client.get("/")
  assert response.status.code == 200;
  assert response.get_json() == {"message": "Hello World"}