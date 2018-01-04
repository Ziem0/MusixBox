import os, sys, subprocess, time, webbrowser
from Models.song import Song
from Models.album import Album
from Models.artist import Artist
from Models.playlist import Playlist


class Controller:

    def __init__(self, view, dao, playlist):
        self.view = view
        self.dao = dao
        self.playlist = playlist


    def add_new_position(self):
        inputs = self.view.new_position_inputs()
        self.dao.create_obj(inputs)


    def searching(self, kind):
        user = self.view.search_inputs(kind)    
        for song in Song.all_songs:
            if song.name.startswith(user) or song.artist.name.startswith(user) or song.album.name.startswith(user) or user == song.album.year:
                self.view.clear_view()
                self.view.print_it(song.artist)
                                
                return song            


    def run_song(self, my_song=None):
        if not my_song:
            self.searching(self.view.title5)
            my_song = self.searching(self.view.title6)
        song = subprocess.Popen(["google-chrome", my_song.link])
        song_lenght = 15
        time.sleep(song_lenght)
        song.kill()


    def end(self):
        self.dao.export_file()
        self.view.print_it(self.view.title4)
        sys.exit()


    def run_yt_search(self): 
        data = self.view.yt_search_input()
        data = data.split()
        link = 'https://www.youtube.com/results?search_query='
        for el in data:
            link += el + '+'

        return webbrowser.open(link)


    def create_playlist(self, name):
        self.playlist.playbook[name] = []


    def add_song_to_playlist(self, name=None, my_song=None):
        if not name and not my_song: 
            self.view.clear_view()
            self.view.print_it(self.playlist)
            name = self.view.playlist_inputs()
            self.searching(self.view.title5)
            my_song = self.searching(self.view.title6)

        if any(title == name for title in self.playlist.playbook.keys()):
            for title,v in self.playlist.playbook.items():
                if title == name:
                    v.append(my_song)
                    
        else:
            self.create_playlist(name)
            self.playlist.playbook[name].append(my_song)

        time.sleep(0.1)
        self.view.print_it(self.view.title7)        
        time.sleep(0.1)


    def run_playlist(self):
        self.view.clear_view()
        self.view.print_it(self.playlist)
        name = self.view.playlist_inputs()
        for k,v in self.playlist.playbook.items():
            if k == name:
                for song in v:
                    self.run_song(song)


    def load_playlist(self):
        data = self.dao.load_playlist()
        for song in data:
            playlist = song[0]
            name = song[1]
            song_name = self.search_load_playlist(name)
            self.add_song_to_playlist(playlist, song_name)


    def search_load_playlist(self, name):
        for song in Song.all_songs:
            if song.name.startswith(name):
                self.view.clear_view()
                self.view.print_it(song.artist)
                            
                return song            
