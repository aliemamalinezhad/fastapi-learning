import json


def test_create_user(client):
    data = {"username": "mrrop",
            "email": "mrrop@example.com",
            "password": "roprop321`"}
    response = client.post("/users/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()['email'] == "mrrop@example.com"
    assert response.json()['is_active'] == True
