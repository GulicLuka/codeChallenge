import os

class ProductConsole:

    def productFunctionsMenu():
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

            option = input("Input your selection: ")

            if option == "1":
                # get all products
                pass
            elif option == "2":
                # get a single product
                pass
            elif option == "3":
                # search products
                pass           
            elif option == "4":
                # limit & skip product
                pass
            elif option == "5":
                # get all prodict categories
                pass
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