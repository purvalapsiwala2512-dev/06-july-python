class FoodOrder:


    def __init__(self, restaurantname, items, totalprice):
        self.restaurantname = restaurantname
        self.items = items
        self.totalprice = totalprice


    def show_order(self):
        print(f"Restaurant:{self.restaurantname}")
        
        for item in self.items:
            print(f"{item}")
        print(f"Total Price:{self.totalprice}")


order = FoodOrder("Haldiram's",["Chole Bhature", "Gulab Jamun", "Lassi"],350)
order.show_order()