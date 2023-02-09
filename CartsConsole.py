import os

class CartConsole:

    def cartFunctionsMenu():
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")

        while True:
            print("*******************************************")
            print()
            print("CARTS")
            print("Select function:")
            print("1:   Get all Carts")
            print("2:   Get a Single Cart")
            print("3:   Get Carts of User")
            print("4:   Add a new Cart")
            print("5:   Update an existing Cart")
            print("6:   Delete Cart")
            print("0:   Back")
            print()
            print("*******************************************")

            option = input("Input your selection: ")

            if option == "1":
                # get all carts
                pass
            elif option == "2":
                # get a single cart
                pass
            elif option == "3":
                # get carts of user
                pass           
            elif option == "4":
                # add cart
                pass
            elif option == "5":
                # update cart
                pass
            elif option == "6":
                # delete cart
                pass
            elif option == "0":
                # go back
                return
            else:
                print("Invalid option, try selecting number from 0 to 6")