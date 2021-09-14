class Notification:
    def __init__(self, title, body):
        self.title = title
        self.body = body
        

    def getDataDict(self, isRedirect, isFinalized= false, redirectPath = None):
    
        dataObj = {
            "title": self.title,
            "body": self.body,
            "isRedirect" : isRedirect,
            "redirectPath" : redirectPath
            "isFinalized" : isFinalized
            
        }
        return dataObj

# noti = Notification("a", "b")
# print(noti.getDataDict(True))   
# 
# topic: orderNumber_userNumber  