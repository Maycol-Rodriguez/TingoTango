class TingoTango:
    def textoTingoTango(self, numero):
        mensaje = ''
        if (numero % 3 == 0):
            mensaje = 'Tingo'
        if (numero % 5 == 0):
            mensaje = 'Tango'
        if (len(mensaje)):
            return mensaje
        else:
            return str(numero)