# Kiểm thử với các trường hợp liên quan đến param
import pytest
import header
import file_handle
import random_email
import requests

user_id = None
create = None
update = None

base_url = "https://gorest.co.in"

@pytest.fixture(params=[
    file_handle.read_file("data_value\\c_p_r.json"),# post param thừa trường "country"
    file_handle.read_file("data_value\\c_p_m.json"),# post param thiếu trường "name"
    file_handle.read_file("data_value\\c_p_w.json") # post param sai trường "email" -> "telephone"
])

def param_error1(request):
    global create
    create = request.param
    return create

@pytest.fixture(params=[
    file_handle.read_file("data_value\\u_p_r.json"),# update param thừa trường "country"
    file_handle.read_file("data_value\\u_p_w.json") # update param sai trường "email" -> "telephone"
])

def param_error2(request):
    global update
    update = request.param
    return update

def test_post_param(param_error1):
    url = base_url + "/public/v2/users"
    headers = header.headers
    global create
    create = param_error1
    create["email"] = random_email.create_random_email()
    response = requests.post(url, headers=headers, json=create)
    print("Test POST: ", response.status_code)
    assert response.status_code == 201


def post():
    url = base_url + "/public/v2/users"
    headers = header.headers
    new_user = file_handle.read_file("data_value\\new_user.json")
    new_user["email"] = random_email.create_random_email()
    response = requests.post(url, headers=headers, json=new_user)
    json_data = response.json()
    assert response.status_code == 201
    global user_id
    user_id = json_data["id"]
    return user_id


def test_put_param(param_error2):
    global user_id
    user_id = post()
    url = base_url + f"/public/v2/users/{user_id}"
    headers = header.headers
    global upadate
    update = param_error2
    response = requests.put(url, headers=headers, json=update)
    print("Test PUT:", response.status_code)
    assert response.status_code == 200

