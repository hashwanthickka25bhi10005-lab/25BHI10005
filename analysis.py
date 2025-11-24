import json

def save_data(user):
    data = {
        "name": user.name,
        "age": user.age,
        "history": user.history
    }
    with open("oral_health_data.json", "w") as f:
        json.dump(data, f, indent=4)

def load_data():
    try:
        with open("oral_health_data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None
