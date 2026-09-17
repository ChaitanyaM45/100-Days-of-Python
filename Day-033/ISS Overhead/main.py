import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 21.6796 # Your latitude
MY_LONG = 92.0266 # Your longitude

email="YOUR MAIL ID"
password="YOUR PASSWORD"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <=MY_LAT+5 and MY_LONG-5 <= iss_longitude <=MY_LONG+5:
        return True
    return False

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/v2", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["sunset"].split("T")[1].split(":")[0])
    print(sunrise)
    print(sunset)
    time_now = datetime.now().hour

    if time_now>=sunset or time_now<=sunrise:
        return True
    return False

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email,password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs="XYZ@gmail.com",
                msg="Subject:Look Up👍\n\nThe ISS is above you in the sky."
            )