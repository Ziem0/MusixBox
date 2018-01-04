from Models.label import Label

class Song(Label):
    all_songs = []

    def __init__(self, album, artist, link,  *args):
        super().__init__(*args)
        self.album = album
        self.artist = artist
        self.link = link

        self.album.add_track(self)
        Song.all_songs.append(self)



