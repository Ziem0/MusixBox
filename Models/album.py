from Models.label import Label

class Album(Label):
    all_albums = []

    def __init__(self, artist, year, *args):
        super().__init__(*args)
        self.artist = artist
        self.year = year
        self.tracks = []

        self.artist.add_album(self)
        Album.all_albums.append(self)

    def add_track(self, song):
        self.tracks.append(song)