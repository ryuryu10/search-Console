import os
import json

def load():
    with open('CONFIG.json') as f:
        json_object = json.load(f)
    return json_object

def isfile():
    if not os.path.isfile('CONFIG.json'):
        return False
    else:
        return True

