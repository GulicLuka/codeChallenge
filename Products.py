import requests
import json

class Products:
    def __init__(self):
        self.url = "https://dummyjson.com/products"


    # get all products
    def getAllProducts(self):
        response = requests.get(self.url)
        
        if response:
            responseJSON = response.json()
            for key, value in responseJSON.items(): 
                if key == "products":
                    print(key + ": ")
                    for product in value:
                        print("--------------------------------------------------------------")
                        for productKey, productValue in product.items():
                            print("     " + productKey + ": ", productValue)
                        print("--------------------------------------------------------------")
                else:
                    print(key + ": ", value)
        else:
            print("Error getting all products")