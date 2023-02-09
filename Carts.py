import requests
import json


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

    # TODO add cart
    def addCart(self):
        pass

    # TODO update cart
    def updateCart(self):
        pass

    # delete cart
    def deleteCart(self, cartID):
        URL = self.url + "/" + cartID

        response = requests.delete(URL)

        if response:
            print("Cart deletd successfully")
        else:
            print("Error deleting cart with ID ( " + cartID + " )")



