class ZomatoOrder:

    def add_items(self,item,quantity=1):
        self.item = item
        self.quamntity = quantity
        print(f"{item}:{quantity}")

z= ZomatoOrder()
z.add_items("Burger")
z.add_items("Burger",2)