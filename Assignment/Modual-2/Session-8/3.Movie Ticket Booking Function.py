def book_movie_ticket(movie_name, seat_type='Regular', snacks=None):
    snacks_display = snacks if snacks else "None"
    print(f"Booking Summary | Movie: {movie_name} | Seat: {seat_type} | Snacks: {snacks_display}")

book_movie_ticket('Jawan', 'VIP', 'Popcorn')

book_movie_ticket(movie_name='Pathaan', seat_type='Recliner', snacks='Nachos')

book_movie_ticket('Jawan', snacks='Popcorn', seat_type='VIP')