import smtplib
from email.mime.text import MIMEText

if __name__ == "__main__":
    my_email = "azzerrt931neu@gmx.de"
    password = "F7W9oxP7ZtbdkH"

    msg = MIMEText('This is a test email')

    msg['Subject'] = 'Test mail'
    msg['From'] = my_email
    msg['To'] = "wasgehtelohd@gmail.com"

    with smtplib.SMTP("mail.gmx.net", port=587) as server:
        server.starttls()
        server.login(user=my_email ,password=password)
        server.sendmail(from_addr=my_email, to_addrs="wasgehtelohd@gmail.com", msg=msg.as_string())