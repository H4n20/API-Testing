import requests
import json
import string
import random

base_url = "https://gorest.co.in"

auth_token = "Bearer e4b8e1f593dc4a731a153c5ec8cc9b8bbb583ae964ce650a741113091b4e2"

def create_random_email():
    domain = "automation.com"
    email_length = 10
    random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range (email_length))
    email = random_string + "@" + domain
    return email

def post_request():
    url = base_url + "/public/v2/users"
    print("post url: " + url)
    headers = {"Authorization": auth_token}
    new_user = {
        "name": "Naveen Automation",
        "email": create_random_email(),
        "gender": "male",
        "status": "active"
    }
    response = requests.post(url, json=new_user, headers=headers)
    json_data = response.json()
    print("Status code:" , response.status_code)
    json_str = json.dumps(json_data, indent=4)
    print("json POST response body: ", json_str)
    user_id = json_data["id"]
    print("user id ===>", user_id)
    assert response.status_code == 201
    assert "name" in json_data
    assert json_data["name"] == "Naveen Automation"
    print(".......POST/Create USER IS DONE.......")
    print(".......=====================.......")
    return user_id

def delete_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    print("DELETE url: " + url)
    headers = {"Authorization": auth_token}
    response = requests.delete(url,headers = headers)
    print("Status code:" , response.status_code)
    assert response.status_code == 204
    print(".......DELETE USER IS DONE.......")
    print(".......=====================.......")


user_id = post_request()
delete_request(user_id)