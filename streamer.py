# Project Title: Music Streaming Service
# Project Description: A simple object-oriented music streaming service that allows users to 
# browse songs and artistes, stream music, and rate tracks.
"""
Created 3 classes:
Song         - This class Handles song tracks in the catalogue.
Artiste      - This class Handles artist with a list of songs.
MusicServer  - This class Manages the catalogue and handles user operations.
"""
#import time module to help simulate streaming duration
import time

# Streaming_timer variable multiplier to make the songs stream in a shorter time. For example, with a multiplier of 20.
Streaming_timer = 20

# Created Song class with attributes title, duration, genre and ratings. It has methods to calculate average rating(average_rating), add a new rating(add_rating), format the average rating for display and a string representation of the song. Ratings are stored as a list of integers.

class Song:
    def __init__(self, title: str, duration: int, genre: str) -> None:
        self.title = title
        self.duration = duration
        self.genre = genre
        self.ratings: list[int] = []

    def average_rating(self) -> float | None:       # Calculate the mean of all submitted ratings.
       
        if not self.ratings:
            return None
        return sum(self.ratings) / len(self.ratings)

    def add_rating(self, rating: int) -> bool:      # Validate that the rating is an integer between 1 and 5, then add it to the ratings list if valid.
        
        if 1 <= rating <= 5:
            self.ratings.append(rating)
            return True
        return False

    def formatted_rating(self) -> str:              # Return the average rating formatted for display. If there are no ratings, it returns 'N/A'. Otherwise, it returns the average rating rounded to two decimal places as a string.
        
        avg = self.average_rating()
        return f"{avg:.2f}" if avg is not None else "N/A"

    def __str__(self) -> str:                       # Return a formatted readable summary of the song, including its title, genre, duration, and average rating.
        
        return (
            f"  '{self.title}' | Genre: {self.genre} | "
            f"Duration: {self.duration}s | Avg Rating: {self.formatted_rating()}"
        )


class Artiste:                                      # Artiste class with attributes name and songs. It has methods to add a song to the artist's catalogue, find a song by title, and provide a string representation of the artist and their songs. The songs attribute is a list of Song objects associated with the artist.
   
    def __init__(self, name: str) -> None:          # Initialize the Artiste with a name and an empty list of songs.
      
        self.name = name
        self.songs: list[Song] = []

    def add_song(self, song: Song) -> None:         # Add a Song to this artist's catalogue.
       
        self.songs.append(song)

    def find_song(self, title: str) -> Song | None: # find_song method performs a case-insensitive search for a song by title within the artist's catalogue. It returns the matching Song object if found, or None if no match is found.
        
        title_lower = title.strip().lower()
        for song in self.songs:
            if song.title.lower() == title_lower:
                return song
        return None

    def __str__(self) -> str:                       # Return a summary of the artist and their songs.
       
        song_titles = ", ".join(f"'{s.title}'" for s in self.songs) or "No songs available"
        return f"{self.name} — Songs: {song_titles}"


# Created a MusicServer class to serve as the main controller that manages the catalogue of artists and songs, and provides operations for browsing, streaming, and rating music. It has methods to add an artist to the service, display available songs and artists, and stream a song based on user input. 

class MusicServer:                                  

    def __init__(self) -> None:
       
        self.artistes: dict[str, Artiste] = {}

    def add_artiste(self, artiste: Artiste) -> None:    # add an artist to the service, using a case-insensitive key in the artistes dictionary to allow for flexible lookups when streaming songs.
       
        self.artistes[artiste.name.lower()] = artiste

    def display_songs(self) -> None:                    # Display all available songs across every artist in the catalogue, along with the artist's name for each song. If no songs are available, it prints the message No songs available.
       
        print("\n--- Available Songs ---")
        any_songs = False
        for artiste in self.artistes.values():
            for song in artiste.songs:
                print(f"{song}  | Artist: {artiste.name}")
                any_songs = True
        if not any_songs:
            print("  No songs available.")

    def display_artistes(self) -> None:                 # Display all available artists and their associated songs. If no artists are available, it prints the message No artistes available.
       
        print("\n--- Available Artistes ---")
        if not self.artistes:
            print("  No artistes available.")
            return
        for artiste in self.artistes.values():
            print(f"  {artiste}")

    def stream_song(self, raw_input: str) -> Song | None:   # Parse a user input string in the format '<song title> by <artiste name>' to identify which song to stream. If the artist or song is not found, it prints an appropriate error message and returns None. If the song is found, it simulates streaming by sleeping for a duration based on the song's length divided by the Streaming_timer multiplier, then returns the streamed Song object.
        
        # Split on ' by ' (case-insensitive) to extract title and artist.
        separator = " by "
        lower_input = raw_input.strip()
        sep_index = lower_input.lower().rfind(separator)

        if sep_index == -1:
            print("  Invalid format. Please use: <song title> by <artiste name>")
            return None

        song_title = lower_input[:sep_index].strip()
        artiste_name = lower_input[sep_index + len(separator):].strip()

        # Look up the artist (case-insensitive).
        artiste = self.artistes.get(artiste_name.lower())
        if artiste is None:
            print(f"  Artiste '{artiste_name}' not found.")
            return None

        # Look up the song within the artist's catalogue.
        song = artiste.find_song(song_title)
        if song is None:
            print(f"  Song '{song_title}' not found for {artiste.name}.")
            return None

        # Streaming the song.
        #stream_seconds = song.duration / Streaming_timer

        # Streaming the song with countdown to show progress.
        stream_seconds = int(song.duration / Streaming_timer)
        print(f"\n  Now streaming '{song.title}' by {artiste.name}...")
        
        for i in range(stream_seconds, 0, -1):          # Code modified to display countdown of remaining seconds while streaming, instead of just sleeping for the entire duration. This provides a more interactive experience for the user.
            print(f"  {i} seconds remaining...")
            time.sleep(1)

        #time.sleep(stream_seconds)
        print("  Finished streaming.\n")
        return song


def prompt_rating(song: Song) -> None:                      # Ask the user whether they want to rate a song, then record the rating. If the user chooses to rate, it prompts for a rating between 1 and 5. The function handles invalid input and allows the user to correct their input without crashing the my streaming app. If a valid rating is submitted, it updates the song's ratings and displays the new average rating.
   
    answer = input("  Would you like to rate this song? (yes/no): ").strip().lower()
    #if answer != "yes":
    # Accept yes/no and y/n for flexibility.
    if answer not in ("yes", "y"):
        return

    while True:
        try:
            rating = int(input("  Enter your rating (1–5): ").strip())
        except ValueError:
            print("  Please enter an integer between 1 and 5.")
            continue

        if song.add_rating(rating):
            print(f"  Thanks! '{song.title}' now has an average rating of {song.formatted_rating()}.")
            break
        else:
            print("  Invalid rating. Please enter a value between 1 and 5.")



def song_catalogue(service: MusicServer) -> None:       # Song catalong function to populate the streaming service with sample set of artists and songs. 

    artiste1 = Artiste("Shakira")
    artiste1.add_song(Song("Waka Waka", 180, "Pop"))
    artiste1.add_song(Song("Deja Vu", 240, "R&B"))

    artiste2 = Artiste("John Lennon")
    artiste2.add_song(Song("Hey Jude", 210, "Pop"))
    artiste2.add_song(Song("Imagine", 195, "Pop"))

    artiste3 = Artiste("2pac")
    artiste3.add_song(Song("Hail Mary", 300, "Rap"))
    artiste3.add_song(Song("By Mama", 195, "Rap"))

    for artiste in (artiste1, artiste2, artiste3):
        service.add_artiste(artiste)


def main() -> None:                         # Main function to runs the music streaming service. It initializes the MusicServer, populates it with a sample catalogue of artists and songs to present in the menu of options to the user. The user can choose to display available songs, display available artists, stream a song by entering its title and artist, or exit the application.
   
    service = MusicServer()
    song_catalogue(service)

    print("Welcome to My Music Streaming App!")
    while True:
        print("\n" + "=" * 40)  # Number of times i want to use the = to create a visual separator in the menu.
        print("  1. Display available songs")
        print("  2. Display available artistes")
        print("  3. Stream a song")
        print("  4. Exit")
        print("=" * 40)

        choice = input("Enter your choice (1–4): ").strip()

        if choice == "1":
            service.display_songs()

        elif choice == "2":
            service.display_artistes()

        elif choice == "3":
            raw = input("\n  Enter '<song title> by <artiste name>': ").strip()
            song = service.stream_song(raw)
            if song:
                prompt_rating(song)

        elif choice == "4":
            print("\nThank you for using this Music Streaming App. Goodbye!")
            break

        else:
            print("  Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()