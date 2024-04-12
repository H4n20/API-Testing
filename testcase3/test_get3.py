import requests
import json
import random
import string

# base URL:
base_url = "https://gorest.co.in"

# authentication token:
auth_token = "Bearer e4b8e1f593dc4a731a153c5ec8cc9b8bbb583ae964ce650a741113091b4e2"


# GET Request
def get_request():
    url = base_url + "/public/v2/users"
    print("GET url: " + url)
    headers = {"Authentication" : auth_token}
    response = requests.get(url, headers=headers)
    print("Status code:" , response.status_code)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json GET response body: ", json_str)
    print(".......GET USER IS DONE.......")
    print(".......=====================.......")

get_request()