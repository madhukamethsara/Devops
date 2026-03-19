from app import app

def test_home():
    client = app.test_client ()
    response = client.get('/')
    assert b"Hello,Devops World! V1" in response.data