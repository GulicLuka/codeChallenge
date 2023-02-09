import os

while True:
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

    print("Select function")
    print("1:   Users")
    print("2:   Carts")
    print("3:   Products")

    option = input("Write number of your selection: ")

    if option == "1":
        # Users functions
        pass
    elif option == "2":
        # Carts functions
        pass
    elif option == "3":
        # Products functions
        pass
    else:
        # invalid selection
        print("Invalid option, try selecting number from 1 to 3")