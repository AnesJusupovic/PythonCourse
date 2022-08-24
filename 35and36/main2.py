import requests
import os
from twilio.rest import Client

if __name__ == "__main__":
    from twilio.rest import Client

    account_sid = 'AC666630fea38b8215ffa737249ac32e8d'
    auth_token = 'd8fe3254611108f3e35b96c54f234fe6'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body='Code: 383192',
        from_='+19403605740',
        to='+4915753695452'
    )
    print(message.sid)
    print(message.status)

