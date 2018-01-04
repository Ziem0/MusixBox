from Controllers.controller import Controller
from Views.view import View
from Dao.dao import Dao
from Models.song import Song
from Models.album import Album
from Models.artist import Artist
from Models.playlist import Playlist

def main():
    
    view = View()
    dao = Dao()
    playlist = Playlist()
    dao.create_obj()
    controller = Controller(view, dao, playlist)
    controller.load_playlist()

    while True:
        controller.view.pause()
        controller.view.clear_view()
        menu = View.create_menu(View.title1, View.main_menu)
        view.print_it(menu)
        user = controller.view.user_choose(view.main_menu)

        if user == 1:
            controller.add_new_position()
        
        elif user == 2:
            controller.add_song_to_playlist()

        elif user == 3:
            controller.run_playlist()

        elif user == 4:
            controller.searching(controller.view.title5)

        elif user == 5:
            controller.run_song()

        elif user == 6:
            controller.run_yt_search()

        elif user == 7:
            controller.dao.save_playlist(playlist.playbook)
            controller.end()


if __name__ == '__main__':
    main()