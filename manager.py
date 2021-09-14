import firebase_admin
from firebase_admin import credentials, messaging
from notification import Notification


cred = credentials.Certificate("market-spaace-firebase-adminsdk-ji1ox-78fda81106.json")
firebase_admin.initialize_app(cred)

def sendPush():
    # See documentation on defining a message payload.
    message = messaging.Message(
        data = {
            "kk":"kk",
            "title": "hi",
            "body": "body"
            
        },
        topic =  "lpl",
    )


    response = messaging.send(message)
    print('Successfully sent message:', response)


sendPush()
# noti = Notification("a", "b")
# print(noti.getDataDict(True))  