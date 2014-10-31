import unittest
from Song import Song


class Test_Song(unittest.TestCase):
    def setUp(self):
        self.song = Song("Title", "Artist", "Album", 1, 160, 120)

    def test_song_init(self):
        self.assertEqual(self.song.artist, "Artist")
        self.assertEqual(self.song.title, "Title")
        self.assertEqual(self.song.album, "Album")
        self.assertEqual(self.song.rate, 1)
        self.assertEqual(self.song.length, 160)
        self.assertEqual(self.song.bitrate, 120)

    def test_rate_if_given_integer_more_than_5_or_less_than_0(self):
        with self.assertRaises(ValueError):
            self.song.rate_song(6)

    def test_rate(self):
        self.song.rate_song(4)
        self.assertEqual(self.song.rate, 4)

    def test_str(self):
        song = "Artist Title - 0:02:40"
        self.assertEqual(str(self.song), song)


if __name__ == '__main__':
    unittest.main()
