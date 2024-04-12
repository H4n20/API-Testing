import requests
import json
import random
import string

# base URL:
base_url = "https://gorest.co.in"

# authentication token:
auth_token = "Bearer e4b8e1f593dc4a731a153c5ec8cc9b8bbb583ae964ce650a741113091b4e"

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

post_request()