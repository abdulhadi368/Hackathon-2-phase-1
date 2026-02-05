from menu import show_menu
from storage import add_item, get_items, update_item, delete_item

while True:
    show_menu()
    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter item name: ")
        add_item(name)
        print("Item added")

    elif choice == "2":
        for item in get_items():
            print(f"{item['id']}. {item['name']}")

    elif choice == "3":
        item_id = int(input("Enter ID to update: "))
        new_name = input("Enter new name: ")
        if update_item(item_id, new_name):
            print("Item updated ✅")
        else:
            print("ID not found ❌")

    elif choice == "4":
        item_id = int(input("Enter ID to delete: "))
        delete_item(item_id)
        print("Item deleted ✅")

    elif choice == "5":
        print("Bye 👋")
        break

    else:
        print("Wrong choice")
