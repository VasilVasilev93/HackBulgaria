import datetime


class Song():
    MAX_RATING = 5
    MIN_RATING = 1

    def __init__(self, title, artist, album, rate, length, bitrate):
        self.title = title
        self.artist = artist
        self.album = album
        self.rate = rate
        self.length = length
        self.bitrate = bitrate

    def rate_song(self, rate):
        if rate < self.MIN_RATING or rate > self.MAX_RATING:
            error_message = "rate must be between %s and %s" % (
                self.MIN_RATING, self.MAX_RATING)
            raise ValueError(error_message)
        self.rate = rate

    def str(self):
        return str(self)

    def __str__(self):
        time = str(datetime.timedelta(seconds=self.length))
        return "{} {} - {}".format(self.artist, self.title, time)
