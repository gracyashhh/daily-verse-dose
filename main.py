# Daily Verse Dose App
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

account_sid = os.getenv("account_sid")
auth_token =  os.getenv("auth_token")
client = Client(account_sid, auth_token)
def sending():
    message = client.messages.create(
        from_=f'whatsapp:+{os.getenv("from")}',
        body=f'whatever',
        to=f'whatsapp:+{os.getenv("to")}'
    )

    print(message.sid)