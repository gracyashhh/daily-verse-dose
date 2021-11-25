# Daily Verse Dose App
from twilio.rest import Client
import os
from cooking_verse import todays_verses
# needed only for local env
# from dotenv import load_dotenv
# load_dotenv()

account_sid = os.getenv("account_sid")
auth_token =  os.getenv("auth_token")
client = Client(account_sid, auth_token)
def sending():
    message = client.messages.create(
        from_=f'whatsapp:+{os.getenv("from")}',
        body=f'{todays_verses["OT"]}\n{todays_verses["NT"]}',
        to=f'whatsapp:+{os.getenv("to")}'
    )

    print(message.sid)