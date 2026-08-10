restaurants = ['Burger Hub', 'Pizza Point', 'Sushi House']
times = [30, 25, 40]

for restaurant, time in zip(restaurants, times):
    print(f"{restaurant} - {time} min")