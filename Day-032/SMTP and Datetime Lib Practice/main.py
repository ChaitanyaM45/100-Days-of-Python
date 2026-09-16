import smtplib
import datetime as dt
import random

now=dt.datetime.now()
weekday=now.weekday()

my_email="test.mail@gmail.com"
password="ENTER YOUR PASSWORD"

if weekday==2:
    with open("./Day-032/SMTP and Datetime Lib Practice/quotes.txt") as quote_file:
        all_quotes=quote_file.readlines()
        quote=random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="XYZ@gmail.com",
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

# import smtplib

# my_email="test.mail@gmail.com"
# password="ENTER YOUR PASSWORD"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="XYZ@gmail.com",
#         msg="Subject: Test Mail\n\nHELLO :)"
#     )

# import datetime as dt
# now=dt.datetime.now()
# print(now) #2026-09-16 16:16:08.521030
# print(now.year) #2026
# print(now.weekday()) #2 ie wednesday as 0:Monday,.......