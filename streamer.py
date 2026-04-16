class Song:
    def __init__(self, title, duration, genre):
        self.title = title
        self.duration = duration
        self.genre = genre
        self.ratings = []

    def average_rating(self):
        if not self.ratings:
            return "N/A"
        return sum(self.ratings) / len(self.ratings)

    def add_rating(self, rating):
        if 1 <= rating <= 5:
            self.ratings.append(rating)
        else:
            print("Invalid rating. Please enter a value between 1 and 5.")      

class Artiste:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)     
