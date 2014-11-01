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

    def save(self, jsonfile):
        songsdict = []
        for item in self.songs:
            songsdict.append(item.__dict__)
        with open(jsonfile, "w") as f:
            json.dump({"Name": self.name, "Songs": songsdict}, f,
                      sort_keys=True, indent=4, separators=(',', ': '))
        return "Playlist: {}, saved succesfully.".format(self.name)

    @staticmethod
    def load(jsonfile):
        with open(jsonfile) as f:
            playlist_to_load = json.loads(f.read())

        newPlaylist = Playlist(playlist_to_load["Name"])
        for item in playlist_to_load["Songs"]:
            newSong = Song(item["title"], item["artist"], item["album"],
                           item["rate"], item["length"], item["bitrate"])
            newPlaylist.add_song(newSong)
        return newPlaylist

new = Playlist("Test Playlist")
song = Song("Title", "Artist", "Album", 5, 20, 120)
song1 = Song("Title1", "Artist1", "Album", 5, 25, 120)
song2 = Song("Title2", "Artist2", "Album", 5, 40, 120)
new.add_song(song)
new.add_song(song1)
new.add_song(song2)

print (new.save('new.json'))
print (Playlist.load('new.json'))
