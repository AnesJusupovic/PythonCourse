##################### Extra Hard Starting Project ######################
import random

import pandas
import smtplib
import datetime as dt
from email.mime.text import MIMEText

if __name__ == "__main__":
    data = pandas.read_csv("birthdays.csv")
    day = dt.datetime.now().day
    month = dt.datetime.now().month
    my_email = "azzerrt931neu@gmx.de"
    password = "F7W9oxP7ZtbdkH"

    for index, row in data.iterrows():
        if row["month"] == month and row["day"] == day:
            choose = random.randint(1, 3)
            with open(f"letter_templates/letter_{choose}.txt") as file:
                text = ""
                count = 0
                for check in file.readlines():
                    if count == 0:
                        print(check)
                        check = check.replace("[NAME]",row["name"])
                        print(check)
                        text += "\n" + check
                    else:
                        text += "\n" + check
                    count += 1
                msg = MIMEText(f'{text}')

                msg['Subject'] = 'Happy Birthday'
                msg['From'] = my_email
                msg['To'] = row["email"]

                with smtplib.SMTP("mail.gmx.net", port=587) as server:
                    server.starttls()
                    server.login(user=my_email, password=password)
                    server.sendmail(from_addr=my_email, to_addrs="wasgehtelohd@gmail.com", msg=msg.as_string())

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




