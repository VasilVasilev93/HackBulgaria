import json
from Playlist import Playlist
from Song import Song


def jdefaultplaylist(o):
    if isinstance(o, Playlist):
        return str(o.str())
    return o.__dict__


def jdefaultsong(o):
    if isinstance(o, Song):
        return str(o.str())
    return o.__dict__

new = Playlist("Test Playlist")
song = Song("Title", "Artist", "Album", 5, 20, 120)
song1 = Song("Title1", "Artist1", "Album", 5, 25, 120)
song2 = Song("Title2", "Artist2", "Album", 5, 40, 120)
new.add_song(song)
new.add_song(song1)
new.add_song(song2)

with open('playlist.json', mode='w', encoding='utf-8') as f:
    for each in new.songs:
        json.dump(each, f, default=jdefaultsong)
        f.write('\n')
