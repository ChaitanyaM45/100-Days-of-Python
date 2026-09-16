import smtplib
import datetime as dt
import pandas as pd
import random

now=dt.datetime.now()
today_tuple=(now.month,now.day)

my_email="test.mail@gmail.com"
password="ENTER YOUR PASSWORD"

df=pd.read_csv("./Day-032/Birthday Wisher/birthdays.csv")

birthday_dict={(data['month'],data['day']):data for (index,data) in df.iterrows()}
if today_tuple in birthday_dict:
    file_path=f"./Day-032/Birthday Wisher/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        birthday_person=birthday_dict[today_tuple]
        content=letter.read()
        content=content.replace("[NAME]",birthday_person['name'])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person['email'],
            msg=f"Subject:Happy Birthday :)\n\n{content}"
        )