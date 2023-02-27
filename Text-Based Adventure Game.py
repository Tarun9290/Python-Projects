#Text-Based Adventure Game: 
#A game where the player makes choices that determine the outcome of the story.

def show_intro():
    print("Welcome to the Text-Based Adventure Game!")
    print("You are in a dark forest and you need to find your way out.")
    print("You come across two paths, one to the left and one to the right.")
    print("Which path do you choose? (left or right)")

def left_path():
    print("You follow the path to the left.")
    print("After a while, you come across a river.")
    print("Do you try to cross the river or go back? (cross or back)")
    choice = input().lower()
    if choice == "cross":
        print("You successfully cross the river and find your way out of the forest.")
        print("Congratulations! You have won the game.")
    elif choice == "back":
        print("You go back and choose the right path instead.")
        right_path()
    else:
        print("Invalid choice. Try again.")
        left_path()

def right_path():
    print("You follow the path to the right.")
    print("After a while, you come across a bear.")
    print("Do you try to fight the bear or run away? (fight or run)")
    choice = input().lower()
    if choice == "fight":
        print("You bravely try to fight the bear, but it is too strong.")
        print("You lose the game.")
    elif choice == "run":
        print("You wisely choose to run and successfully escape the bear.")
        print("You find your way out of the forest.")
        print("Congratulations! You have won the game.")
    else:
        print("Invalid choice. Try again.")
        right_path()

show_intro()
choice = input().lower()
if choice == "left":
    left_path()
elif choice == "right":
    right_path()
else:
    print("Invalid choice. Try again.")
    show_intro()
