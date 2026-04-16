import unittest
from streamer import Song, Artiste, MusicServer   


class TestMusicSystem(unittest.TestCase):

    def test_add_song_to_artiste(self):
        # Arrange
        artiste = Artiste("2pac")
        song = Song("Dear Mama", 180, "Rap")

        # Act
        artiste.add_song(song)

        # Assert
        self.assertEqual(len(artiste.songs), 1)
        self.assertEqual(artiste.songs[0].title, "Dear Mama")

    def test_add_multiple_songs_to_artiste(self):
        # Arrange
        artiste = Artiste("2pac")
        song1 = Song("Hail Mary", 300, "Rap")
        song2 = Song("By Dear Mama", 195, "Rap")

        # Act
        artiste.add_song(song1)
        artiste.add_song(song2)

        # Assert
        self.assertEqual(len(artiste.songs), 2)

    def test_song_title_contains_by(self):
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

    
    def test_song_title_has_by_word(self):
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

 
    def test_add_multiple_artistes(self):
        # Arrange
        server = MusicServer()
        artiste1 = Artiste("Shakira")
        artiste2 = Artiste("2pac")

        # Act
        server.add_artiste(artiste1)
        server.add_artiste(artiste2)

        # Assert
        self.assertEqual(len(server.artistes), 2)

    def test_case_insensitive_artiste(self):
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