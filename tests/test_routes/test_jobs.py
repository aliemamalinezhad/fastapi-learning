import json


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
