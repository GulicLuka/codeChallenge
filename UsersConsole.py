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

            # used just to get parameters
            #users.getParameters()

            if option == "1":
                # get all users
                users.getAllUsers()
            elif option == "2":
                # get a single user
                userID = input("Insert user ID: ")
                if userID.isnumeric():
                    users.getUserByID(userID=userID)
                else:
                    print("Invalid input for ID")
            elif option == "3":
                # search user
                query = input("Insert query to search for users: ")
                users.getUsersSearch(query=query)
            elif option == "4":
                # filter users
                limit = input("number of items you would like to get (0 - get all items): ")
                skip = input("number of items you would like to skip: ")
                selections = UserConsole.getSelections(keys=users.getParameterKeys())
                print("Write value into the one you want to filter, only first one will be used others will be ignored:")
                filter = UserConsole.getValues(keys=users.getParameterKeys())
                users.getUsersFilter(skip=skip, limit=limit, selections=selections, filter=filter)
            elif option == "5":
                # limit & skip user
                limit = input("number of items you would like to get (0 - get all items): ")
                skip = input("number of items you would like to skip: ")
                selections = UserConsole.getSelections(keys=users.getParameterKeys())
                users.getUsersLimit(limit=limit, skip=skip, selections=selections)
            elif option == "6":
                # get user's carts
                userID = input("Insert user ID: ")
                if userID.isnumeric():
                    users.getUserCartsByID(userID=userID)
                else:
                    print("Invalid input for ID")
            elif option == "7":
                # get user's posts
                userID = input("Insert user ID: ")
                if userID.isnumeric():
                    users.getUserPostsByID(userID=userID)
                else:
                    print("Invalid input for ID")
            elif option == "8":
                # get user's todos
                userID = input("Insert user ID: ")
                if userID.isnumeric():
                    users.getUserTodosByID(userID=userID)
                else:
                    print("Invalid input for ID")
            elif option == "9":
                # add user
                print("Input user data")
                inputDict = UserConsole.getValues(keys=users.getParameterKeys())
                users.addUser(inputDict=inputDict)
                pass
            elif option == "10":
                # update user
                userID = input("Input user ID that you want to update: ")
                if userID.isnumeric():
                    print("Input user data that you want to update")
                    inputDict = UserConsole.getValues(keys=users.getParameterKeys())
                    users.updateUser(userID=userID,inputDict=inputDict)
                else:
                    print("Invalid input for ID")
                    
            elif option == "11":
                # delete user
                userID = input("Insert user ID: ")
                if userID.isnumeric():
                    users.deleteUser(userID=userID)
                else:
                    print("Invalid input for ID")
            elif option == "0":
                # go back
                return
            else:
                print("Invalid option, try selecting number from 0 to 11")

    def getSelections(keys):
        for i, key in enumerate(keys):
            print(i,key)

        selectString = input("write comma separated numbers, that you want to select from list above: ")
        if len(selectString) > 1:
            itemIDs = selectString.split(",")
        else:
            itemIDs = list(selectString)

        itemIDsInt = []
        for item in itemIDs:
            if item.isnumeric():
                try:
                    num = int(item)
                    if num < len(keys):
                        itemIDsInt.append(num)
                except Exception:
                    pass
        try:        
            selections = map(keys.__getitem__, itemIDsInt)
        except Exception:
            print("Invalid input")
            return None
        return list(selections)
    
    def getValues(keys):
        inputDict = {}
        for key in keys:
            if "." in key:
                inputMessage = " ".join(key.split(".")) + ": "
                value = input(inputMessage)
            else:
                value = input(key + ": ")
            inputDict[key] = value
        return inputDict