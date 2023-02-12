import requests
import json
from mergedeep import merge

class Carts:
    def __init__(self):
        self.url = "https://dummyjson.com/carts"

    # get all carts
    def getAllCarts(self):
        response = requests.get(self.url)
        
        if response:
            responseJSON = response.json()
            for cart in responseJSON["carts"]:
                print("--------------------------------------------------------------")
                for cartKey, cartValue in cart.items():
                    if cartKey == "products":
                        print(cartKey + ": ")
                        for product in cartValue:
                            print("/////////////////////////////////////////////////")
                            for productKey, productValue in product.items():
                                print("     " + productKey + ": ", productValue)
                            print("/////////////////////////////////////////////////")
                    else:
                        print(cartKey + ": ", cartValue)
                print("--------------------------------------------------------------")
        else:
            print("Error getting all carts")
        
    # get cart with ID
    def getCartByID(self, cartID):
        URL = self.url + "/" + cartID

        response = requests.get(URL)

        if response:
            responseJSON = response.json()
            print("--------------------------------------------------------------")
            for cartKey, cartValue in responseJSON.items():
                if cartKey == "products":
                    print(cartKey + ": ")
                    for product in cartValue:
                        print("/////////////////////////////////////////////////")
                        for productKey, productValue in product.items():
                            print("     " + productKey + ": ", productValue)
                        print("/////////////////////////////////////////////////")
                else:
                    print(cartKey + ": ", cartValue)
            print("--------------------------------------------------------------")
        else:
            print("Error getting cart with ID ( " + cartID + " )")

    # get carts of a user
    def getUserCarts(self, userID):
        URL = self.url + "/user/" + userID

        response = requests.get(URL)

        if response:
            responseJSON = response.json()
            print("--------------------------------------------------------------")
            for cartKey, cartValue in responseJSON.items():
                if cartKey == "products":
                    print(cartKey + ": ")
                    for product in cartValue:
                        print("/////////////////////////////////////////////////")
                        for productKey, productValue in product.items():
                            print("     " + productKey + ": ", productValue)
                        print("/////////////////////////////////////////////////")
                else:
                    print(cartKey + ": ", cartValue)
            print("--------------------------------------------------------------")
        else:
            print("Error getting user carts with ID ( " + userID + " )")

    # add cart
    def addCart(self, inputList):
        URL = self.url + "/add"
        
        data = {"userId": 1, "products": inputList}

        response = requests.post(
            URL,
            headers={
                "Content-Type": "application/json"
            },
            data=json.dumps(data)
            )
    
        if response:
            print("Cart added successfuly")
            print(response.json())
        else:
            print("Error adding new Cart")

    # update cart
    def updateCart(self, inputList, cartID):
        URL = self.url + "/" + cartID
        

        wrongInput = True
        while wrongInput:
            mergeExistingData = input("Do you want to merge with existing cart (y - YES, n - NO):")
            if mergeExistingData == "y" or mergeExistingData == "n":
                wrongInput = False
        
        if mergeExistingData == "y":
            mergeData = True
        else:
            mergeData = False

        data = {"merge": mergeData, "userId": 1, "products": inputList}

        response = requests.put(
            URL,
            headers={
                "Content-Type": "application/json"
            },
            data=json.dumps(data)
            )
    
        if response:
            print("Cart updated successfuly")
            print(response.json())
        else:
            print("Error updating Cart")

    # delete cart
    def deleteCart(self, cartID):
        URL = self.url + "/" + cartID

        response = requests.delete(URL)

        if response:
            print("Cart deletd successfully")
        else:
            print("Error deleting cart with ID ( " + cartID + " )")

    