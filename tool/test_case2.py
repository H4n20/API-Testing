
import pytest
import requests
import header
import file_handle
import random_email

user_id = None
user_id1 = None
user_id2 = None

base_url = "https://gorest.co.in"

@pytest.fixture(params=[
    header.miss_headers,
    header.wrong_headers
])

def error_headers(request):
    return request.param

def post():
    url = base_url + "/public/v2/users"
    headers = header.headers
    new_user = file_handle.read_file("data_value\\new_user.json")
    new_user["email"] = random_email.create_random_email()
    response = requests.post(url, json=new_user, headers=headers)
    json_data = response.json()
    global user_id
    user_id = json_data["id"]
    print(response.status_code)
    assert response.status_code == 201

def test_get_auth(error_headers):
    url = base_url + "/public/v2/users"
    headers = error_headers
    response = requests.get(url, headers=headers)
    print("Test GET:", response.status_code)
    assert response.status_code == 200


def test_post_auth(error_headers):
    url = base_url + "/public/v2/users"
    headers = error_headers
    new_user = file_handle.read_file("data_value\\new_user.json")
    new_user["email"] = random_email.create_random_email()
    response = requests.post(url, json=new_user, headers=headers)
    json_data = response.json()
    global user_id
    user_id = json_data["id"]
    print("Test POST: ", response.status_code)
    assert response.status_code == 201


def test_put_auth(error_headers):
    global user_id
    global user_id1
    global user_id2

    if(error_headers == header.wrong_headers):
        user_id2 = post()
        user_id = user_id2

    if(error_headers == header.miss_headers):
        user_id1 = post()
        user_id = user_id1
    url = base_url + f"/public/v2/users/{user_id}"
    headers = error_headers
    update_user = file_handle.read_file("data_value\\update_user.json")
    update_user["email"] = random_email.create_random_email()
    response = requests.put(url, json=update_user, headers=headers)
    print("Test PUT:", response.status_code)
    assert response.status_code == 200


def test_delete_auth(error_headers):
    global user_id
    global user_id1
    global user_id2
    if(error_headers == header.wrong_headers):
        user_id = user_id2
    if(error_headers == header.miss_headers):
        user_id = user_id1
    url = base_url + f"/public/v2/users/{user_id}"
    headers = error_headers
    response = requests.delete(url, headers=headers)
    print("Test DELETE: ", response.status_code)
    assert response.status_code == 204


