
#To-Do List: 
#
#Create a program that allows the user to add and remove items from a list,
#and view the list.


todo_list = []

while True:
    # get user input
    action = input("What would you like to do? (add/remove/view) ")

    # add item to list
    if action == "add":
        item = input("Enter an item to add: ")
        todo_list.append(item)
        print("Item added.")

    # remove item from list
    elif action == "remove":
        item = input("Enter an item to remove: ")
        todo_list.remove(item)
        print("Item removed.")

    # view list
    elif action == "view":
        print("Here is your list:")
        for item in todo_list:
            print(item)

    # invalid input
    else:
        print("Invalid input.")
