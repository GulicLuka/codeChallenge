import requests
import json

class Products:
    def __init__(self):
        self.url = "https://dummyjson.com/products"
        self.parameters = ['id', 'title', 'description', 'price', 'discountPercentage', 'rating', 'stock', 'brand', 'category', 'thumbnail', 'images']

    # getter method
    def getParameterKeys(self):
        return self.parameters

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


    # build url for skip and limit
    def skipLimitUrl(self, skip, limit, url):
        if limit.isnumeric():
            url += "?limit=" + limit
        elif skip.isnumeric():
            url += "?skip=" + skip
        
        if limit.isnumeric() and skip.isnumeric():
            url += "&skip=" + skip
        return url
    
    # build url for selections
    def selectItems(self, skip, limit, selections, url):
        URL = self.skipLimitUrl(skip=skip, limit=limit, url=url)

        if selections is None:
            selections = self.getParameterKeys()
        
        if not limit.isnumeric() and not skip.isnumeric() and all(el in self.getParameterKeys() for el in selections):
            URL += "?select="
            selectLen = len(selections)

            for i, item in enumerate(selections):
                if "." in item:
                    if i == selectLen - 1:
                        URL += item.split(".")[0]
                    else:
                        URL += item.split(".")[0] + ","
                else:
                    if i == selectLen - 1:
                        URL += item
                    else:
                        URL += item + ","

        
        if (limit.isnumeric() or skip.isnumeric()) and all(el in self.getParameterKeys() for el in selections):
            URL += "&select="

            selecLen = len(selections)

            for i, item in enumerate(selections):
                if "." in item:
                    if i == selecLen - 1:
                        URL += item.split(".")[0]
                    else:
                        URL += item.split(".")[0] + ","
                else:
                    if i == selecLen - 1:
                        URL += item
                    else:
                        URL += item + ","
        return URL


    # TODO limit and skip products
    def limitSkipProducts(self, limit, skip, selections):
        URL = self.selectItems(skip=skip, limit=limit, selections=selections, url=self.url)
        
        if URL is not None:
            response = requests.get(URL)

            if response:
                responseJSON = response.json()
                for product in responseJSON["products"]:
                    print("--------------------------------------------------------------")
                    for productKey, productValue in product.items():
                        print(productKey + ": ", productValue)
                    print("--------------------------------------------------------------")
            else:
                print("Error with request")
        else:
            print("invalide input parameters")


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

    
    def getParameters(self):
        URL = self.url + "/1" 
        response = requests.get(URL)

        if response:
            responseJSON = response.json()
            parameters = self.parameterRecursion(JSON=responseJSON, d="")
            print(parameters)

    def parameterRecursion(self, JSON, d=""):
        if not isinstance(JSON, dict):
            return [ d ]
        
        par = []
        for key, value in JSON.items():
            if isinstance(value, dict):
                if d == "":
                    par.extend(self.parameterRecursion(JSON[key], d+key))
                else:
                    par.extend(self.parameterRecursion(JSON[key], d+"."+key))
            else:
                if d == "":
                    par.extend(self.parameterRecursion(key, d+key))
                else:
                    par.extend(self.parameterRecursion(key, d+"."+key))
        return par