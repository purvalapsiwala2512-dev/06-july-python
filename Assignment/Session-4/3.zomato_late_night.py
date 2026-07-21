age = int(input("Enter your age: "))
current_time = int(input("Enter the current time in 24-hour format: "))


if age >= 18:
    
    if current_time >= 22 or current_time <= 2:
        print("Order allowed. Happy late-night snacking!")
    else:
        print("Order not allowed. Late-night menu items are only open between 10 PM and 2 AM.")
else:
    print("Order not allowed. You must be 18 or older to place an order during these hours.")