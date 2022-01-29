import json
from random import randint
from sqlalchemy import null

def add_user(user):
    with open("users.json") as reader:
        data = json.load(reader)
    
    data[f"user_{user.user_id}"] = user.to_json()
    
    
    with open("users.json", "w") as writer:
        json.dump(data, writer, ensure_ascii=False, indent=4)

def add_time(time):
    with open("users.json") as reader:
        data = json.load(reader)

    user = data.get(f"user_{time.user_id}", null)
    if user:
        user["times"].append(time.get_time())
        
        with open("users.json", "w") as writer:
            json.dump(data, writer, ensure_ascii=False, indent=4)

def get_users():
    with open("users.json", "r") as reader:
        data = json.load(reader)
    
    return data