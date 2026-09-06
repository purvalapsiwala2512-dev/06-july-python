class User:
    
    def __init__(self,username,email):
        self.username = username
        self.email = email

    def display(self):
        print(f"Username:{self.username} and email:{self.email}")

u = User("Purva","purvalapsiwala@gmail.com")
u.display()