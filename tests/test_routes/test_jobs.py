import json
from fastapi import status

def test_create_job(client):
    data = {
        "title": "job number one",
        "company": "hideliner",
        "company_url": "www.hideliner.ir",
        "location": "Iran, Tehran",
        "description": "python",
        "date_posted": "2022-02-04",

    }
    response = client.post("/jobs/create-job/", json.dumps(data))
    assert response.status_code == 200
    assert response.json()["company"] == "hideliner"
    assert response.json()["description"] == "python"


def test_read_job(client):
    data = {
        "title": "job number one",
        "company": "hideliner",
        "company_url": "www.hideliner.ir",
        "location": "Iran, Tehran",
        "description": "python",
        "date_posted": "2022-02-04",
    }

    response = client.post("/jobs/create-job/", json.dumps(data))
    response = client.get("/jobs/get/1/")

    assert response.status_code == 200
    assert response.json()['title'] == "job number one"


def test_read_jobs(client):
    data = {
        "title": "SDE super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "python",
        "date_posted": "2022-03-20",
    }
    client.post("/jobs/create-job/", json.dumps(data))
    client.post("/jobs/create-job/", json.dumps(data))

    response = client.get("/jobs/all/")

    assert response.status_code == 200
    assert response.json()[0]
    assert response.json()[1]


def test_update_a_job(client):
    data = {
        "title": "New Job super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "fastapi",
        "date_posted": "2022-03-20"
        }
    client.post("/jobs/create-job/",json.dumps(data))
    data["title"] = "test new title"
    response = client.put("/jobs/update/1/",json.dumps(data))
    assert response.json()["msg"] == "Successfully updated data."

def test_delete_job(client):
    data = {
        "title": "New Job super",
        "company": "doogle",
        "company_url": "www.doogle.com",
        "location": "USA,NY",
        "description": "fastapi",
        "date_posted": "2022-03-20"
    }
    client.post("/jobs/create-job/", json.dumps(data))
    msg = client.delete("/jobs/delete/1/")
    response = client.get("/jobs/get/1/")

    assert response.status_code == status.HTTP_404_NOT_FOUND
