import requests

BASE_URL = "http://127.0.0.1:5000"
tasks = []

def test_create_task():
    new_task_data = {
        "title": "Testes unitários",
        "description": "Testando o pytest"
    }

    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.staus_code == 200