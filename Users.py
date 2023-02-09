import requests
import json
import os

class Users:
    def __init__(self):
        self.url = 'https://dummyjson.com/users'
    
    def getAllUsers(self):
        response = requests.get(self.url)
        
        if response:
            responseJSON = response.json()
            for user in responseJSON["users"]:
                print("--------------------------------")
                for key, value in user.items():
                    print(key + ": ", value)
                print("--------------------------------")