import requests
import json
import os

class Users:
    def __init__(self):
        self.url = 'https://dummyjson.com/users'
    
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

    # TODO skip and limit users
    def getUsersLimit(self):
        pass

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
