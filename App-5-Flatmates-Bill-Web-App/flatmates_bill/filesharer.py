from filestack import Client
from dotenv import dotenv_values

# Import Environment variables from .env file
env = dotenv_values()
api_key = env["API_KEY"]

class FileSharer():

    def __init__(self, filepath, api_key=api_key):
        self.filepath = filepath
        self.api_key = api_key
        
    def share(self):
        cli = Client(apikey = self.api_key)
        filelink = cli.upload(filepath = self.filepath)
        
        return filelink.url