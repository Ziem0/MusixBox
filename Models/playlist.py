from Models.song import Song 


class Playlist:

    def __init__(self):
        self.playbook = {}

    def __str__(self):
        out = '\t\tPLaylists baby!\n'
        if not self.playbook:
            return 'Playbook is empty!\n'
        else:
            for k,v in self.playbook.items():
                out += '\n'+str(k)+':'+'\n\n'
                for song in v:
                    if v:
                        out += "{}\n".format(song.name)
                    else:
                        return 'Empty list!'
            return out

    