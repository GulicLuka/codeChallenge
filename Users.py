import requests
import json

class Users:
    def __init__(self):
        self.url = 'https://dummyjson.com/users'
        self.parameters = ['id', 'firstName', 'lastName', 'maidenName', 'age', 'gender', 'email', 'phone', 'username', 'password', 'birthDate', 'image', 'bloodGroup', 'height', 'weight', 'eyeColor', 'hair.color', 'hair.type', 'domain', 'ip', 'address.address', 'address.city', 'address.coordinates.lat', 'address.coordinates.lng', 'address.postalCode', 'address.state', 'macAddress', 'university', 'bank.cardExpire', 'bank.cardNumber', 'bank.cardType', 'bank.currency', 'bank.iban', 'company.address.address', 'company.address.city', 'company.address.coordinates.lat', 'company.address.coordinates.lng', 'company.address.postalCode', 'company.address.state', 'company.department', 'company.name', 'company.title', 'ein', 'ssn', 'userAgent']
    
    # getter method
    def getParameterKeys(self):
        return self.parameters

    # get all users
    def getAllUsers(self):
        response = requests.get(self.url)
        
        if response:
            responseJSON = response.json()
            for user in responseJSON["users"]:
                print("--------------------------------------------------------------")
                for key, value in user.items():
                    print(key + ": ", value)
                print("--------------------------------------------------------------")
        else:
            print("Error getting all users")

    # get single user with given ID
    def getUserByID(self, userID):
        URL = self.url + "/" + userID

        response = requests.get(URL)

        if response:
            responseJSON = response.json()
            print("--------------------------------------------------------------")
            for key, value in responseJSON.items():
                print(key + ": ", value)
            print("--------------------------------------------------------------")
        else:
            print("Error getting user with ID ( " + userID + " )")

    # get users that match the query
    def getUsersSearch(self, query):
        URL = self.url + "/search?q=" + query

        response = requests.get(URL)

        if response:
            responseJSON = response.json()
            for user in responseJSON["users"]:
                print("--------------------------------------------------------------")
                for key, value in user.items():
                    print(key + ": ", value)
                print("--------------------------------------------------------------")
        else:
            print("Error getting users that match query ( " + query + " )")
        
    # TODO filter users
    def getUsersFilter(self):
        pass

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

    # skip and limit users
    def getUsersLimit(self, limit, skip, selections):
        URL = self.selectItems(skip=skip, limit=limit, selections=selections, url=self.url)

        if URL is not None:
            response = requests.get(URL)

            if response:
                responseJSON = response.json()
                for user in responseJSON["users"]:
                    print("--------------------------------------------------------------")
                    for userKey, userValue in user.items():
                        print(userKey + ": ", userValue)
                    print("--------------------------------------------------------------")
            else:
                print("Error with request")
        else:
            print("invalide input parameters")

    # get user's carts
    def getUserCartsByID(self, userID):
        URL = self.url + "/" + userID + "/carts"

        response = requests.get(URL)

        if response:
            responseJSON = response.json()
            print("--------------------------------------------------------------")
            for cart in responseJSON["carts"]:
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
            print("Error getting user's carts with ID ( " + userID + " )")

    # get user's posts
    def getUserPostsByID(self, userID):
        URL = self.url + "/" + userID + "/posts"

        response = requests.get(URL)

        if response:
            responseJSON = response.json()
            print("--------------------------------------------------------------")
            for key, value in responseJSON.items():
                if key == "posts":
                    for post in value:
                        print("/////////////////////////////////////////////////")
                        for postKey, postValue in post.items():
                            print("     " + postKey + ": ", postValue)
                        print("/////////////////////////////////////////////////")
                else:
                    print(key + ": ", value)
            print("--------------------------------------------------------------")
        else:
            print("Error getting user's posts with ID ( " + userID + " )")

    # get user's todos
    def getUserTodosByID(self, userID):
        URL = self.url + "/" + userID + "/todos"

        response = requests.get(URL)

        if response:
            responseJSON = response.json()
            print("--------------------------------------------------------------")
            for key, value in responseJSON.items():
                if key == "todos":
                    for todo in value:
                        print("/////////////////////////////////////////////////")
                        for todoKey, todoValue in todo.items():
                            print("     " + todoKey + ": ", todoValue)
                        print("/////////////////////////////////////////////////")
                else:
                    print(key + ": ", value)
        else:
            print("Error getting user's todos with ID ( " + userID + " )")

    # TODO add new user
    def addUser(self):
        pass

    # TODO update user
    def updateUser(self):
        pass

    # delete user
    def deleteUser(self, userID):
        URL = self.url + "/" + userID

        response = requests.delete(URL)

        if response:
            print("user deleted succesfully")
        else:
            print("Error deleting user with ID ( " + userID + " )")

    
    # helper methods
    # get user dict keys
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
    
            
