from Models.label import Label

class Artist(Label):
    all_artists = []

    def __init__(self, *args):
        super().__init__(*args)
        self.albums = []
        Artist.all_artists.append(self)

    def add_album(self, album):
        self.albums.append(album)