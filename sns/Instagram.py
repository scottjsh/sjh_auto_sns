from instagrapi import Client

class Instagram:
    def __init__(self, username: str, password: str):
        self.__client = Client()
        self.__client.login(username, password)
        
    def uploadPhotoToStory(self, imagePath):
        self.__client.photo_upload_to_story(imagePath)