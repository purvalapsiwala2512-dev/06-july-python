class User :

    college = "abc"
    def __init__(self,name,email):
        self.name = name
        self.email = email

    def run(self):
        print(self.name,self.email,self.collage)

    @classmethod
    def display(cls):
        print(cls.collage)

    @staticmethod
    def sample():
        print("static method")

User.collage="xyz"

u = User("test","test@gmail.com")
u.run()


# u1 = User("test1","test1@gmail.com")
# u1.rum()

User.display()
# User.sample(10)
