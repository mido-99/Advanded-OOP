from dotenv import dotenv_values
import requests

# Import Environment variables from .env file
env = dotenv_values()
api = env["api_news"]


class NewsFeed:
    '''Generate Recent News Feed for personal interests and send them as an email'''
    
    base_url = "https://newsapi.org/v2/everything?"
    
    def __init__(self, topic="NASA", from_date='2023-06-15', to_date='2023-06-20', lang='en'):
        self.topic = topic
        self.from_date = from_date
        self.to_date = to_date
        self.lang = lang

    def get(self):
        # Get the response content in json format
        res = requests.get(f"{self.base_url}qInTitle={self.topic}"\
                            f"&from={self.from_date}&to={self.to_date}"\
                            f"&Language={self.lang}&apiKey={api}")
        
        articles = res.json()['articles']
        
        # Extract desired data & create the email body
        return self._build_email(articles)

    def _build_email(self, articles):
        email_body = ''
        
        for article in articles:
            title = article['title']
            url = article['url']
            
            email_body += f"{title}\n{url}\n\n"
        
        return email_body


if __name__ == '__main__':
    news = NewsFeed().get()
    print(news)
