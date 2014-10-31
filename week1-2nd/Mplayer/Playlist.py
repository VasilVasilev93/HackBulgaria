import datetime
import json
from Song import Song


class Playlist():
    MAX_RATING = 5
    MIN_RATING = 1
    MIN_BITRATE = 60

    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song_name):
        for each in range(0, len(self.songs)):
            if (song_name == self.songs[each].title):
                del self.songs[each]
                break

    def total_length(self):
        total_length = 0
        for each in range(0, len(self.songs)):
            total_length += self.songs[each].length

        return total_length

    def remove_disrated(self, rating):
        if rating < self.MIN_RATING or rating > self.MAX_RATING:
            error_message = "Rating must be between %s and %s" % (
                self.MIN_RATING, self.MAX_RATING)
            raise ValueError(error_message)
        for each in range(0, len(self.songs)):
            if self.songs[each].rate < rating:
                self.remove_song(self.songs[each].title)
                return self.remove_disrated(rating)

    def remove_bad_quality(self):
        for each in range(0, len(self.songs)):
            if self.songs[each].bitrate < self.MIN_BITRATE:
                self.remove_song(self.songs[each].title)
                return self.remove_bad_quality()

    def show_artists(self):
        artists = []
        for each in range(0, len(self.songs)):
            artists.append(self.songs[each].artist)
        return set(artists)

    def str(self):
        currentsongs = []
        for each in range(0, len(self.songs)):
            currentsongs.append(str(self.songs[each]))
            print (str(currentsongs[each]))
        return currentsongs

    def jdefaultplaylist(self, o):
        if isinstance(o, Playlist):
            return str(o.str())
        return o.__dict__

    def jdefaultsong(self, o):
        if isinstance(o, Song):
            return str(o.str())
        return o.__dict__

    def save(self, file_name):
        with open(file_name, mode='w', encoding='utf-8') as f:
            for each in self.songs:
                json.dump(each, f, default=self.jdefaultsong)
                f.write('\n')
            f.close()
        return "Playlist: {}, saved succesfully.".format(self.name)

    def __str__(self):
        currentsongs = []
        for each in range(0, len(self.songs)):
            time = str(datetime.timedelta(seconds=self.songs[each].length))
            song = "{} {} - {}".format(
                self.songs[each].artist, self.songs[each].title, time)
            currentsongs.append(song)
        return str(currentsongs)

new = Playlist("Test Playlist")
song = Song("Title", "Artist", "Album", 5, 20, 120)
song1 = Song("Title1", "Artist1", "Album", 5, 25, 120)
song2 = Song("Title2", "Artist2", "Album", 5, 40, 120)
new.add_song(song)
new.add_song(song1)
new.add_song(song2)

print (new.save('new.json'))
