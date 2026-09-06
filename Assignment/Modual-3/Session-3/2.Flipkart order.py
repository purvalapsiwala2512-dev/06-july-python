try:
    price = float(input("Enter item price:"))
    quantity = int(input("Enter quantity:"))
    
    total = price * quantity
    print("Order Total:", total)
except ValueError:
    print("Error: Please enter valid numbers!")