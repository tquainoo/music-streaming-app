import unittest                                     # Importing the unittest module to create unit tests for the music streaming app. 
from streamer import Song, Artiste, MusicServer     # Importing the Song, Artiste, and MusicServer classes from the streamer module to be tested in the TestMusicApp class.


class TestMusicApp(unittest.TestCase):           # Test class for the music streaming App that inherits from unittest.TestCase to create unit tests for the Song, Artiste, and MusicServer classes.

    def test_add_song_to_artiste(self):             # Test method to verify that a song can be added to an artiste's song list and that the song's details are correctly stored.
        # Arrange
        artiste = Artiste("2pac")
        song = Song("Dear Mama", 180, "Rap")

        # Act
        artiste.add_song(song)

        # Assert
        self.assertEqual(len(artiste.songs), 1)
        self.assertEqual(artiste.songs[0].title, "Dear Mama")

    def test_add_multiple_songs_to_artiste(self):             # Test method to verify that multiple songs can be added to an artiste's song list.
        # Arrange
        artiste = Artiste("2pac")
        song1 = Song("Hail Mary", 300, "Rap")
        song2 = Song("By Dear Mama", 195, "Rap")

        # Act
        artiste.add_song(song1)
        artiste.add_song(song2)

        # Assert
        self.assertEqual(len(artiste.songs), 2)

    def test_song_title_contains_by(self):       # Test method to verify that a song with "by" as part of a word in the title can be streamed correctly from the music server.
        # Arrange
        server = MusicServer()
        artiste = Artiste("2pac")
        song = Song("Dear ByMama", 210, "Rap")

        artiste.add_song(song)
        server.add_artiste(artiste)

        # Act
        result = server.stream_song("Dear byMama by 2pac")

        # Assert
        self.assertIsNotNone(result)
        self.assertEqual(result.title, "Dear ByMama")
        self.assertEqual(result.genre, "Rap")

    
    def test_song_title_has_by_word(self):      # Test method to verify that a song with "by" as a separate word in the title can be streamed correctly from the music server.# This test checks that the streaming functionality can handle song titles that include "by" as a word, ensuring that the correct song is retrieved based on the provided title and artiste name.

        # Arrange
        server = MusicServer()
        artiste = Artiste("2pac")
        song = Song("By Mama", 210, "Rap")

        artiste.add_song(song)
        server.add_artiste(artiste)

        # Act
        result = server.stream_song("By Mama by 2pac")

        # Assert
        self.assertIsNotNone(result)
        self.assertEqual(result.title, "By Mama")
        self.assertEqual(result.genre, "Rap")

 
    def test_add_multiple_artistes(self):       # Test method to verify that multiple artistes can be added to the music server and that they are stored correctly in the server's artiste list. This test ensures that the server can manage multiple artistes without any issues.    
        # Arrange
        server = MusicServer()
        artiste1 = Artiste("Shakira")
        artiste2 = Artiste("2pac")

        # Act
        server.add_artiste(artiste1)
        server.add_artiste(artiste2)

        # Assert
        self.assertEqual(len(server.artistes), 2)

    def test_case_insensitive_artiste(self):    # Test method to verify that the music server can handle artiste names in a case-insensitive manner when adding artistes. This test checks that the server stores artiste names in lowercase and can retrieve them correctly regardless of the case used when adding or streaming songs.
        # Arrange
        server = MusicServer()
        artiste = Artiste("Shakira")

        # Act
        server.add_artiste(artiste)

        # Assert
        self.assertIn("shakira", server.artistes)
        self.assertNotIn("Shakira", server.artistes)  # stored as lowercase

    

if __name__ == "__main__":
    unittest.main()