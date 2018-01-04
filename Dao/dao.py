import csv
import os, sys
from Models.song import Song
from Models.album import Album
from Models.artist import Artist

class Dao:

    @staticmethod
    def import_file():
        if not os.path.isfile('Dao/dao.csv'):
            raise FileNotFoundError
        else:
            lista = []
            with open('Dao/dao.csv', 'r') as f:
                for line in f:
                    line = line.strip()
                    line = line.split(',')
                    lista.append(line)

        return lista

    @staticmethod
    def create_obj(user=None):
        if not user:
            data = Dao.import_file()
            n = 1
            author = data[0]
            artist = Artist(author[0])
            album = Album(artist, author[2], author[1])
            song = Song(album, artist, author[4], author[3])
        else:
            n = 0            
            data = [user]  
            
        for item in data[n:]:
            for song in Song.all_songs:

                if item[0] == song.artist.name and item[1] == song.album.name:
                    artist = song.artist
                    album = song.album
                    song = Song(album, artist, item[4], item[3])
                    break

                elif item[0] == song.artist.name and item[1] != song.album.name:
                    artist = song.artist
                    album = Album(artist, item[2], item[1])
                    song = Song(album, artist, item[4], item[3])
                    break
                    
                elif item[0] != song.artist.name:
                    artist = Artist(item[0])
                    album = Album(artist, item[2], item[1])
                    song = Song(album, artist, item[4], item[3])
                    break

    @staticmethod
    def export_file():
        with open('Dao/dao.csv', 'w') as f:
            writer = csv.writer(f)
            for song in Song.all_songs:
                writer.writerow([song.artist.name, song.album.name, song.album.year, song.name, song.link])

    @staticmethod
    def save_playlist(playlist):
        with open('Dao/playlist.csv', 'w') as file:
            writer = csv.writer(file)
            for k,v in playlist.items():
                for song in v:
                    writer.writerow([k, song.name])

    @staticmethod
    def load_playlist():
        lista = []
        with open('Dao/playlist.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                lista.append(row)

        return lista

