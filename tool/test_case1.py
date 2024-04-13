import pytest
import requests
import header
import file_handle
import random_email

user_id = None

base_url = "https://gorest.co.in"

def test_get():
    url = base_url + "/public/v2/users"
    headers = header.headers
    response = requests.get(url, headers=headers)
    print("Test GET:",response.status_code)
    assert response.status_code == 200


def test_post():
    url = base_url + "/public/v2/users"
    headers = header.headers
    new_user = file_handle.read_file("data_value\\new_user.json")
    new_user["email"] = random_email.create_random_email()
    response = requests.post(url, json=new_user, headers=headers)
    json_data = response.json()
    global user_id
    user_id = json_data["id"]
    print("Test POST: ", response.status_code)
    assert response.status_code == 201


def test_put():
    global user_id
    url = base_url + f"/public/v2/users/{user_id}"
    headers = header.headers
    update_user = file_handle.read_file("data_value\\update_user.json")
    update_user["email"] = random_email.create_random_email()
    response = requests.put(url, json=update_user, headers=headers)
    print("Test PUT:", response.status_code)
    assert response.status_code == 200


def test_delete():
    global user_id
    url = base_url + f"/public/v2/users/{user_id}"
    headers = header.headers
    response = requests.delete(url, headers=headers)
    print("Test DELETE: ", response.status_code)
    assert response.status_code == 204


