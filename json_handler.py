import json
import os



def check_json(name):
    return os.path.isfile(name)
    
def create_json():
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump([], f, indent=4)


def write_json(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

def read_json():
    try:
        with open("data.json" ,"r") as f:
            content = f.read().strip()
            if not content: 
                data = []
            else: 
                data = json.loads(content)
    except:
        print("Error")
    return data