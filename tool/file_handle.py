import json

def read_file(path):
    try:
        with open(path, "r") as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print("File Not Found")
        return None
