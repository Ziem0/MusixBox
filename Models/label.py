class Label:

    def __init__(self, name):
        self.name = name
        

    def __call__(self):
        dictt = vars(self)
        out = '| '
        if self.__class__.__name__ == 'Artist':
            for k,v in dictt.items():
                if not isinstance(v, list):
                    out += "{}:{} |\n".format(k,v)
            for k,v in dictt.items():
                if isinstance(v, list):
                    for album in v:
                        out += "\n|{}:{}\n".format(k,album)
                

        elif self.__class__.__name__ == 'Album':
            for k,v in dictt.items():
                if not isinstance(v, Label) and not isinstance(v, list):
                    out += "{}:{} | ".format(k,v)
            for k,v in dictt.items():
                if isinstance(v, list):
                    for n,track in enumerate(v,1):
                        out += "\n|{}:{}".format(n,track.name)

        return out


    def __str__(self):
        main_line = self()
        lenght = len(main_line)
        out = '-'*lenght + '\n' + main_line + '\n' + '-'*lenght

        return main_line