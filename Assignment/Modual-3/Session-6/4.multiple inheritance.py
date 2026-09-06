class Influencer:

    def __init__(self,username,followers):
        self.username = username
        self.followers = followers

class Brand:
    def __init__(self,brandname):
        self.brand_name = brandname


class BrandPartner(Influencer,Brand):
    def __init__(self, username, followers,brandname):
        super().__init__(username, followers)
        Brand.__init__(self,brandname)


    def display(self):
        print(self.username,self.followers,self.brandname)

d = BrandPartner("Purva",80000,"One8")
d.display()