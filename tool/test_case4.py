
import pytest
import random_email
import header
import file_handle
import requests

new_user = None

base_url = "https://gorest.co.in"

@pytest.fixture(params=[
    file_handle.read_file("data_value\\dup_id.json"),# post trùng id
    file_handle.read_file("data_value\\dup_email.json"),# post trùng email
    file_handle.read_file("data_value\\wformat_email.json") # post sai định dạng email
])

def data_error(request):
    global new_user
    new_user = request.param
    return new_user

def test_post_data(data_error):
    url = base_url + "/public/v2/users"
    headers = header.headers
    new_user = data_error
    if(new_user == file_handle.read_file("data_value\\dup_id.json")):
        new_user["email"] = random_email.create_random_email()
    response = requests.post(url, headers=headers, json=new_user)
    print("Test POST: ", response.status_code)
    assert response.status_code == 201
