# Create multiple classes representing different notification channels (Email, SMS, and Push).
# Each channel class should implement the send method.
# Create a function that accepts any object and calls its send method. The object should be able to handle the 
                                                                # notification, even if its class is unknown
# demonstrate the above irrespective of type

class Email:
    def send(self):
        print("This is the Email Channel")
class SMS:
    def send(self):
        print("This  is SMS channel")
class push:
    def send(self):
        print("This is push channel")
def accept(obj):
    if hasattr(obj,"send"):
        obj.send()
e=Email()
accept(e)
s=SMS()
accept(s)
p=push()
accept(p)