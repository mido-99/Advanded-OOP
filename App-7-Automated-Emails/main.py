from dotenv import dotenv_values
from pprint import pprint
import requests

# Import Environment variables from .env file
env = dotenv_values()
api = env["api_news"]


class NewsFeed:
    
    def __init__(self, data):
        self.data = data
        
    def get(**kwargs):
        topic = 'tesla'
        from_date = '2023-06-15'
        to_date = '2023-06-20'
        
        res = requests.get(f"https://newsapi.org/v2/everything?qintitle={topic}\
                            &from={from_date}&to={to_date}&language=en&apiKey={api}")
        
        pprint(res.text)

