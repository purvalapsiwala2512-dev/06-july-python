class Demo:

    name = "test"
    _email = "test@gmail.com"
    __age = 30

    def test(self):
        print(self.name,self._email,self.__age)

d = Demo()
d.name="purva"
d._email="xyz@gmail.com"
d._Demo__age=100
d.test()