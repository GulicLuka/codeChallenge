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

    # get a single product
    def getProductByID(self, productID):
        URL = self.url + "/" + productID

        response = requests.get(URL)

        if response:
            responseJSON = response.json()
            print("--------------------------------------------------------------")
            for key, value in responseJSON.items():
                print(key + ": ", value)
            print("--------------------------------------------------------------")
        else:
            print("Error getting product with ID ( " + productID + " )")

    # get product by query
    def searchProducts(self, query):
        URL = self.url + "/search?q=" + query
        
        response = requests.get(URL)
        
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
            print("Error getting products that match query ( " + query + " )")

    # TODO limit and skip products
    def limitSkipProducts(self):
        pass

    # get all products categories
    def getProductsCategories(self):
        URL = self.url + "/categories"

        response = requests.get(URL)

        if response:
            responseJSON = response.json()
            print("--------------------------------------------------------------")
            for category in responseJSON: 
                print(category)
            print("--------------------------------------------------------------")

        else:
            print("Error getting products categories")

    #TODO get products of category
    def getProductsOfCategory(self, category):
        pass

    #TODO add new product
    def addProduct(self):
        pass

    #TODO update product
    def updateProduct(self):
        pass

    # delete product
    def deleteProduct(self, productID):
        URL = self.url + "/" + productID

        response = requests.delete(URL)

        if response:
            print("user deleted succesfully")
        else:
            print("Error deleting user with ID ( " + productID + " )")