import os
import json

def load():
    with open('CONFIG.json') as f:
        json_object = json.load(f)
    return json_object

def isfile():
    if os.path.isfile('CONFIG.json'):
        return True
    else:
        return False

def make():
    f = open('CONFIG.json', 'w')
    f.close()