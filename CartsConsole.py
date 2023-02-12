import os
from Carts import Carts
from Products import Products

class CartConsole:

    def cartFunctionsMenu():
        carts = Carts()
        products = Products()

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
            print("7:   Search filter")
            print("0:   Back")
            print()
            print("*******************************************")

            option = input("Input your selection: ")

            if option == "1":
                # get all carts
                carts.getAllCarts()
            elif option == "2":
                # get a single cart
                cartID = input("Insert cart ID: ")
                if cartID.isnumeric():
                    carts.getCartByID(cartID=cartID)
                else:
                    print("Invalid input for ID")
            elif option == "3":
                # get carts of user
                userID = input("Insert user ID: ")
                if userID.isnumeric():
                    carts.getUserCarts(userID=userID)
                else:
                    print("Invalid input for ID")       
            elif option == "4":
                # add cart
                print("Input cart data")
                inputList = CartConsole.getValues(products)
                carts.addCart(inputList=inputList)
            elif option == "5":
                # update cart
                cartID = input("Insert cart ID: ")
                if cartID.isnumeric():
                    print("Update cart with items")
                    inputList = CartConsole.getValues(products)
                    carts.updateCart(inputList=inputList, cartID=cartID)
                else:
                    print("Invalid input for ID")
            elif option == "6":
                # delete cart
                cartID = input("Insert cart ID: ")
                if cartID.isnumeric():
                    carts.deleteCart(cartID=cartID)
                else:
                    print("Invalid input for ID")
            elif option == "7":
                searchInput = input("search Carts by: ")
                carts.searchFilter(searchInput=searchInput)
            elif option == "0":
                # go back
                return
            else:
                print("Invalid option, try selecting number from 0 to 7")

    def getValues(products):
        products.limitSkipProducts(limit="0", skip="0", selections=["id", "title"])

        inputList = []

        continueSelection = "y"

        while continueSelection == "y":
            tempDict = {}

            while True:
                selection = input("Number of selected product: ")
                try:
                    selection = int(selection)
                    break
                except Exception:
                    continue
            
            while True:
                quantity = input("Quantity of selected product: ")
                try:
                    quantity = int(quantity)
                    break
                except Exception:
                    continue

            tempDict["id"] = selection
            tempDict["quantity"] = quantity

            inputList.append(tempDict)

            wrongInput = True
            while wrongInput:
                continueSelection = input("Do you want to add another item (y - YES, n - NO): ")
                if continueSelection == "y" or continueSelection == "n":
                    wrongInput = False

        return inputList