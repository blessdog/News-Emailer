import yagmail
import pandas
from news import NewsFeed
import datetime
import time


def send_email():
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=yesterday,
                         to_date=today)

    email = yagmail.SMTP(user="1cooldumpster@gmail.com", password="lanpolawankchwgh")
    email.send(to=row['email'],
               subject=f"Your {row['interest']} news for today.",
               contents=f"Hi {row['name']}\n See whats on about {row['interest']} today. \n{news_feed.get()}\n")


while True:
    if datetime.datetime.now().hour == 17 and datetime.datetime.now().minute == 43:
        df = pandas.read_csv('people.csv')

        for index, row in df.iterrows():
            send_email()

    time.sleep(60)

