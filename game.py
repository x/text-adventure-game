def location_1(has_key):
    print("You're in a beautiful field.")
    print("ACTION MENU:")
    print("- walk east")
    print("- walk west")
    if not has_key:
        print("- pickup key")

    action = input("INPUT ACTION: ")

    if action == "walk east":
        print("You walk east towards a house.")
        location_2(has_key)
    elif action == "walk west":
        print("You walk west. The field continues.")
        location_4(has_key)
    elif action == "pickup key" and not has_key:
        print("You pick up the key.")
        has_key = True
        location_1(has_key)
    else:
        print(f"Invalid action: {action}")
        location_1(has_key)


def location_2(has_key):
    print("You see a house with a locked door.")
    print("ACTION MENU:")
    print("- walk west")
    if has_key:
        print("- use key")

    action = input("INPUT ACTION: ")

    if action == "walk west":
        location_1(has_key)
    elif action == "use key" and has_key:
        location_3(has_key)
    else:
        print(f"Invalid action: {action}")
        location_2(has_key)


def location_3(has_key):
    print("You enter the house. You won!")


def location_4(has_key):
    print("You fall into a pit, GAME OVER")


def main():
    has_key = False
    location_1(has_key)


main()
