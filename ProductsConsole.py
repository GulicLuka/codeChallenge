import os
from Products import Products

class ProductConsole:

    def productFunctionsMenu():
        products = Products()

        if os.name == "posix":
            os.system("clear")
        else:
            os.system("cls")

        while True:
            print("*******************************************")
            print()
            print("USERS")
            print("Select function:")
            print("1:   Get all Products")
            print("2:   Get a Single Product")
            print("3:   Search Products")
            print("4:   Limit & Skip Products")
            print("5:   Get all Products Categories")
            print("6:   Get Product of Category")
            print("7:   Add a new Product")
            print("8:   Update an existing Product")
            print("9:   Delete Product")
            print("0:   Back")
            print()
            print("*******************************************")

            # used just to get parameters
            #products.getParameters()

            option = input("Input your selection: ")

            if option == "1":
                # get all products
                products.getAllProducts()
            elif option == "2":
                # get a single product
                productID = input("Insert user ID: ")
                if productID.isnumeric():
                    products.getProductByID(productID=productID)
                else:
                    print("Invalid input for ID")
            elif option == "3":
                # search products
                query = input("Insert query to search for users: ")
                products.searchProducts(query=query)      
            elif option == "4":
                # limit & skip product
                limit = input("number of items you would like to get (0 - get all items): ")
                skip = input("number of items you would like to skip: ")
                selections = ProductConsole.getSelections(keys=products.getParameterKeys())
                products.limitSkipProducts(limit=limit, skip=skip, selections=selections)
            elif option == "5":
                # get all prodict categories
                products.getProductsCategories()
            elif option == "6":
                # get product of category
                pass
            elif option == "7":
                # add product
                pass
            elif option == "8":
                # update product
                pass
            elif option == "9":
                # delete product
                pass
            elif option == "0":
                # go back
                return
            else:
                print("Invalid option, try selecting number from 0 to 9")


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