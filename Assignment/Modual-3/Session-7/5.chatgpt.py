class Notification:

    def send(self):
        print("You 7 unread message")

class Email(Notification):

    def send(self):
        print("You have 20 email")

class SMS(Notification):

    def send(self):
        print("You have 20 SMS")

n = Notification()
n.send()

e = Email()
e.send()

s = SMS()
s.send()