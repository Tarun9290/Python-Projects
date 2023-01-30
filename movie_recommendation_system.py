#Movie Recommendation Engine:
#Build a program that recommends movies to users based on their viewing history and preferences.

class User:
    def __init__(self, name):
        self.name = name
        self.watched_movies = []
        self.favorites = []

    def add_movie(self, movie):
        self.watched_movies.append(movie)

    def add_favorite(self, movie):
        self.favorites.append(movie)

class Movie:
    def __init__(self, title, genre):
        self.title = title
        self.genre = genre

def recommend_movies(user, movies):
    # Get list of unwatched movies
    unwatched_movies = [movie for movie in movies if movie not in user.watched_movies]

    # Filter unwatched movies by user's favorite genres
    recommended_movies = [movie for movie in unwatched_movies if movie.genre in user.favorites]

    return recommended_movies

# Example usage:

# Create list of movies
movies = [Movie("The Shawshank Redemption", "Drama"),
          Movie("The Godfather", "Crime"),
          Movie("The Dark Knight", "Action"),
          Movie("The Lord of the Rings", "Fantasy"),
          Movie("Pulp Fiction", "Crime"),
          Movie("The Good, the Bad and the Ugly", "Western")]

# Create user
user = User("John")

# Add some movies to user's watched list
user.add_movie(movies[0])
user.add_movie(movies[1])
user.add_movie(movies[2])

# Add some genres to user's favorites
user.add_favorite("Crime")
user.add_favorite("Action")

# Recommend movies
recommended = recommend_movies(user, movies)

# Print recommended movies
for movie in recommended:
    print(movie.title)
