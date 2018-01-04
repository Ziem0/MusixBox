import os 

class View:

    main_menu = ['add new position', 'add song to playlist', 'run playlist', 'advanced searching', 'run song', 'yt search', 'exit' ]

    title1 = 'Menu: '
    title2 = 'Searching options'
    title3 = 'What do you want to do?'
    title4 = 'byebye'
    title5 = 'type artist or album or year or song: '
    title6 = 'type song title: '
    title7 = 'task completed!'

    @staticmethod
    def clear_view():
        os.system('clear')

    @staticmethod
    def pause():
        input('Press enter to continue...\n')    

    @staticmethod
    def print_it(it):
        print(it)

    @staticmethod
    def user_choose(menu):
        user = 0
        while user < 1 or user > len(menu):
            try:
                user = int(input('choose options: '))
            except ValueError:
                print('Wrong number!')
            
        return user

    @staticmethod
    def create_menu(title,main_menu):
        out = '\t' + title + '\n\n'
        for n,opt in enumerate(main_menu,1):
            out += "{}. {}\n".format(n, opt)
        return out     

    @staticmethod
    def new_position_inputs():
        artist = input('artist: ').lower()    
        album = input('album: ').lower()
        year = input('year: ').lower()
        song = input('song: ').lower()
        link = input('link: ').lower()
        return artist, album, year, song, link

    @staticmethod
    def search_inputs(kind):
        what = input(kind).lower()
        return what            

    @staticmethod
    def yt_search_input():
        data = input('artist name and song title: ').lower()
        return data

    @staticmethod
    def playlist_inputs():
        data = input('type playlist name: ').lower()
        return data    
        