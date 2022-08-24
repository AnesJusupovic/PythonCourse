import time

import requests
from datetime import datetime as dt
import smtplib
import random
from email.mime.text import MIMEText

MY_LAT = 51.507351
MY_LONG = -0.127758

def is_iss_overhead():
    parameters = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LONG + 5 and MY_LONG - 5 >= iss_longitude <= iss_longitude + 5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "long": MY_LONG,
        "formatted": 0
    }
    parameters = {"lat": MY_LAT,
                  "long": MY_LONG,
                  "formatted": 0}
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = dt.now().hour
    if time_now >= sunset or time_now <= sunrise:
        return True

if __name__ == "__main__":
    my_email = "azzerrt931neu@gmx.de"
    password = "F7W9oxP7ZtbdkH"

    msg = MIMEText("Look at the sky!")

    msg['Subject'] = 'Look Up\n\nThe ISS is above you in the sky.'
    msg['From'] = my_email
    msg['To'] = "wasgehtelohd@gmail.com"

    while True:
        time.sleep(60)
        if is_iss_overhead() and is_night():
            with smtplib.SMTP("mail.gmx.net", port=587) as server:
                server.starttls()
                server.login(user=my_email, password=password)
                server.sendmail(from_addr=my_email,
                                to_addrs="wasgehtelohd@gmail.com",
                                msg=msg.as_string())

