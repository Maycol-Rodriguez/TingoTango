class TingoTango:
    def TingoTango(self, numero):
        if (numero % 15 == 0):
            return (f'{numero} Tingo Tango')
        elif (numero % 3 == 0):
            return (f'{numero} Tingo')
        elif (numero % 5 == 0):
            return (f'{numero} Tango')
        else:
            return (f'{numero}')