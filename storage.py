data = []

def add_item(name):
    data.append({"id": len(data)+1, "name": name})

def get_items():
    return data

def find_item(item_id):
    for item in data:
        if item["id"] == item_id:
            return item
    return None

def update_item(item_id, new_name):
    item = find_item(item_id)
    if item:
        item["name"] = new_name
        return True
    return False

def delete_item(item_id):
    global data
    data = [item for item in data if item["id"] != item_id]
