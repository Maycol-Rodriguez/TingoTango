class TingoTango:
    def TingoTango(self, numero):
        if (numero % 15 == 0):
            return 'TingoTango'
        elif (numero % 3 == 0):
            return 'Tingo'
        elif (numero % 5 == 0):
            return 'Tango'