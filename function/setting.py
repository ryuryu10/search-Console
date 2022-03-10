import json
global path

def path(dir):
    global path
    path = dir

def load():
    global path
    with open(path, 'r') as f:
        json_data = json.load(f)
    return json_data

def view():
    return load()
