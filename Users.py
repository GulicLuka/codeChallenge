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