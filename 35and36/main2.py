import requests
import os
from twilio.rest import Client

if __name__ == "__main__":

    account_sid = os.environ.get("ASID")
    auth_token = os.environ.get("ATOKEN")
    print(account_sid)
    print(auth_token)
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='Code: 383192',
        from_='+19403605740',
        to='+4915753695452'
    )
    print(message.sid)
    print(message.status)

