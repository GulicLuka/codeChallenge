import os
from Users import Users

class UserConsole:

    def userFunctionsMenu():
        users = Users()
        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")

        while True:
            print("*******************************************")
            print()
            print("USERS")
            print("Select function:")
            print("1:   Get all Users")
            print("2:   Get a Single User")
            print("3:   Search Users")
            print("4:   Filter Users")
            print("5:   Limit & Skip Users")
            print("6:   Get User's carts")
            print("7:   Get User's posts")
            print("8:   Get User's todos")
            print("9:   Add a new User")
            print("10:  Update an existing User")
            print("11:  Delete User")
            print("0:   Back")
            print()
            print("*******************************************")

            option = input("Input your selection: ")

            if option == "1":
                # get all users
                users.getAllUsers()
            elif option == "2":
                # get a single user
                pass
            elif option == "3":
                # search user
                pass           
            elif option == "4":
                # filter users
                pass
            elif option == "5":
                # limit & skip user
                pass
            elif option == "6":
                # get user's carts
                pass
            elif option == "7":
                # get user's posts
                pass
            elif option == "8":
                # get user's todos
                pass
            elif option == "9":
                # add user
                pass
            elif option == "10":
                # update user
                pass
            elif option == "11":
                # delete user
                pass
            elif option == "0":
                # go back
                return
            else:
                print("Invalid option, try selecting number from 0 to 11")