import unittest
from Playlist import Playlist
from Song import Song


class Test_playlist(unittest.TestCase):

    def setUp(self):
        self.testplaylist = Playlist("Test Playlist")
        self.song = Song("Title", "Artist", "Album", 5, 20, 120)
        self.song1 = Song("Title1", "Artist", "Album1", 1, 20, 50)
        self.song2 = Song("Title2", "Artist1", "Album1", 1, 20, 100)
        self.testplaylist.add_song(self.song)
        self.testplaylist.add_song(self.song1)
        self.testplaylist.add_song(self.song2)

    def test_playlist_init(self):
        self.assertEqual(self.testplaylist.name, "Test Playlist")

    def test_playlist(self):
        self.assertEqual(self.testplaylist.songs[0], self.song)

    def test_remove_song(self):
        self.testplaylist.remove_song("Title1")
        self.assertEqual(self.testplaylist.songs[0], self.song)
        self.assertEqual(self.testplaylist.songs[1], self.song2)

    def test_total_length(self):
        self.assertEqual(self.testplaylist.total_length(), 60)

    def test_remove_disrated(self):
        self.testplaylist.remove_disrated(4)
        self.assertEqual(self.testplaylist.songs[0], self.song)

    def test_remove_bad_quality(self):
        self.testplaylist.remove_bad_quality()
        self.assertEqual(self.testplaylist.songs[0], self.song)
        self.assertEqual(self.testplaylist.songs[1], self.song2)

    def test_show_artists(self):
        artists = ["Artist", "Artist1"]
        self.assertSetEqual(self.testplaylist.show_artists(), set(artists))


if __name__ == '__main__':
    unittest.main()
