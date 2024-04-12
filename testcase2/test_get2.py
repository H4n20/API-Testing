# Test GET requesst mà không có token xác thực
import requests
import json

# base URL:
base_url = "https://gorest.co.in"

# GET Request
def get_request():
    url = base_url + "/public/v2/users"
    print("GET url: " + url)
    response = requests.get(url)
    print(response.status_code)
    assert response.status_code == 200
    json_data = response.json()
    json_str = json.dumps(json_data, indent=4)
    print("json GET response body: ", json_str)
    print(".......GET USER IS DONE.......")
    print(".......=====================.......")

get_request()
