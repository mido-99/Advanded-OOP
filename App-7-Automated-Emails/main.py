import yagmail
from dotenv import dotenv_values
import pandas
from news_feed import NewsFeed
import datetime, time


# Create a sender email instance
password = dotenv_values()["moh_pass"]
email = yagmail.SMTP("momhahah9@gmail.com", password=password)

# Get email addresses from database
df = pandas.read_excel("people.xlsx")

# Today's date
today = datetime.datetime.now().date()
yesterday = (today - datetime.timedelta(1))
today = str(today)
yesterday = str(yesterday)

## Multiple emails ##
while True:
        
    # Runnig the loop in a certain time
    if datetime.datetime.now().hour == 10 and datetime.datetime.now().minute == 0:
        time.sleep(60)
        
        for index, row in df.iterrows():
        
            # Create the news feed
            news = NewsFeed(topic=row['Interest'], from_date=yesterday, to_date=today).get()
            
            # Send email to each person with their interest
            email.send(to=row["Email"], 
                    subject=f"Today's News about {row['Interest']}!", 
                    contents=f"Hi {row['Name']}\n"\
                            f"These are some news about {row['Interest']} we've collected for you:\n\n"\
                            f"{news}")

## For one email ##
# for index, row in df.iterrows():

#     # Create the news feed
#     news = NewsFeed(topic=row['Interest'], from_date=yesterday, to_date=today).get()
    
#     # Send email to each person with their interest
#     email.send(to=row["Email"], 
#             subject=f"Today's News about {row['Interest']}!", 
#             contents=f"Hi {row['Name']}\n"\
#                     f"These are some news about {row['Interest']} we've collected for you:\n\n"\
#                     f"{news}")
