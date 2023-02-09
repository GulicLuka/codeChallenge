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