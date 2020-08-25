class Lamp:
    _LAMPS = [''' 
              .
         .    |    ,
          \   '   /
           ` ,-. '
        --- (   ) ---
             \ /
            _|=|_
           |_____|
        ''',
        '''
             ,-.
            (   )
             \ /
            _|=|_
           |_____|
     ''']


    def __init__(self, is_turned_on):# metodo init -> es el constructor de la clase
        self.__is_turned_on = is_turned_on


    def turn_on(self): #metodo publico
        self.__is_turned_on = True
        self._display_image()


    def turn_off(self):# metodo publico
        self.__is_turned_on = False
        self._display_image()

    
    def _display_image(self):#metodo privadpo
        if self.__is_turned_on:
            print(self._LAMPS[0])
        else:
            print(self._LAMPS[1])


