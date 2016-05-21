from __future__ import division
from math import sqrt


class Estadisticas:
    def __init__(self, elementos):
        self.n = 0
        self.elementos = elementos
        self.horapico = []
        self.demandaPicoHora = []
        self.cont = 1
        try:
            self.elementos = map(int, elementos)
        except ValueError:
            self.elementos.pop()
            self.elementos = map(int, elementos)


    def media(self):
        med = 0
        for i in self.elementos:
            med += i
        med/=len(self.elementos)
        return med

    def varianza(self):
        var = 0
        for i in self.elementos:
            var += (i- self.media())** 2
        var/=len(self.elementos)
        return var

    def desviacion(self):
        return sqrt(self.varianza())
