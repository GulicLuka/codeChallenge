
import requests

class SaveImage:

    def saveImageLocally(imageUrl):
        response = requests.get(imageUrl)
        if response:
            urlSplit = imageUrl.split("/")
            fileName = urlSplit[-1]
            file = open(fileName, "wb")
            file.write(response.content)
            file.close()
