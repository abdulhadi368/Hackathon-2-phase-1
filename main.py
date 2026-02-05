from menu import show_menu
from storage import add_item, get_items

while True:
    show_menu()
    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter item name: ")
        add_item(name)
        print("Item added")

    elif choice == "2":
        print(get_items())

    elif choice == "3":
        print("Bye 👋")
        break

    else:
        print("Wrong choice")
