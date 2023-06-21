import yagmail
from dotenv import dotenv_values
import pandas
from news_feed import NewsFeed


# Create a sender email instance
password = dotenv_values()["moh_pass"]
email = yagmail.SMTP("momhahah9@gmail.com", password=password)

# Get email addresses from database
df = pandas.read_excel("people.xlsx")


for index, row in df.iterrows():
    
    # Create the news feed
    news = NewsFeed(topic=row['Interest']).get()
    
    # Send email to each person with their interest
    email.send(to=row["Email"], 
            subject=f"Today's News about {row['Interest']}!", 
            contents=f"Hi {row['Name']}\n"\
                    f"These are some news about {row['Interest']} we've collected for you.\n\n"\
                    f"{news}")












# df = pandas.DataFrame([["Name", "Email", "Interest"],
#                         ["Soso", "lihevo4293@anwarb.com", "Space"],
#                         ["Lolo", "xzavier.edel@donebyngle.com", 'Football'],
#                         ["Toto", "pawefibe@afia.pro", "Maths"]])

# df.to_excel("newpeople.xlsx", header=False, index=False)

