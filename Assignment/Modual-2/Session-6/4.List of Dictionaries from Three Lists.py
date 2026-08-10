titles = ["Inception", "Interstellar", "The Dark Knight"]
genres = ["Sci-Fi", "Sci-Fi", "Action"]
ratings = [8.8, 8.7, 9.0]

movies = [
    {"title": title, "genre": genre, "rating": rating}
    for title, genre, rating in zip(titles, genres, ratings)
]

print("Movie Catalog:")
print(movies)