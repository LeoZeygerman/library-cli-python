import json

def load_data():
    try:
        with open('data/books.json', 'r') as f:
            return json.load(f)
    except:
        return []
    
def save_data(data):
    with open('data/books.json', 'w') as f:
        return json.dump(data, f)