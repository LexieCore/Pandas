from stats import Estadisticas as stats
import data
import sys
import datetime
import pickle
from termcolor import colored
import pandas
from selenium import webdriver

p = data.Pandax()

class Analisis:

    def __init__(self,folder):
        self.folder = folder
        self.semanas =p.get_weeks(p.extractAll(folder))

    def horapico(self,valor):
        '''Funcion que recibe un (valor DF) y produce una lista con la media aritmetica de cada hora (1,23)'''
        dias = 0
        horas = {k: [0] for k in range(1,24)}
        for element in self.semanas:
            pandax = []
            ds = []
            for i in range(len(self.semanas[element])):
                f = self.semanas[element][i]+".mexico.txt"
                try:
                    demanda = p.jsontopanda(f,valor).astype(int)
                except ValueError:
                    demanda = p.jsontopanda(f,valor)[:23].astype(int)
                for i,e in enumerate(demanda):
                    horas[i+1] += e
                dias += 1
        return horas

    def diaspico(self,valor):
        '''Funcion que recibe un valor (columna DF) y produce la media aritmetica respecto la demanda ordenada por los dias de la semnana (lunes, domingo)'''
        dias = 0
        dias = {k: [] for k in range(7)}
        del self.semanas['semana5']
        for element in self.semanas:
            for i in range(len(self.semanas[element])):
                f = self.semanas[element][i]+".mexico.txt"
                try:
                    demanda = p.jsontopanda(f,valor).astype(int)
                except ValueError:
                    demanda = p.jsontopanda(f,valor)[:23].astype(int)
                s = stats(demanda)
                s = s.media()
                dias[i] += [s]
        for i,e in enumerate(dias):
            s = stats(dias[e])
            s = s.media()
            dias[e] = s
        return dias

    def mediaPorDia(self,valor):
        '''Funcion que recibe un valor (columna DF) y regresa una lista con la media aritmetica diaria y semanal respecto a la demanda por cada semana (semana1-semana5)'''
        diaria = {}
        for element in self.semanas:
            data = []
            for i in range(len(self.semanas[element])):
                f = self.semanas[element][i]+".mexico.txt"
                try:
                    demanda = p.jsontopanda(f,valor).astype(int)
                except ValueError:
                    demanda = p.jsontopanda(f,valor)[:23].astype(int)
                s = stats(demanda)
                s = s.media()
                data.append(s)
            diaria[element] = data
        semanal = {}
        for e in diaria:
            s = stats(diaria[e])
            semanal[e] = s.media()
        return diaria,semanal

    def desviacionPorSemana(self,semanas):
        '''Funcion que produce una desviacion estandar por semana (semana1-semana5)'''
        for e in semanas:
            s = stats(semanas[e])
            s = s.desviacion()
            #s = s.media()
            semanas[e] = s
        return semanas

    def desviacionSemanal(self,semanas):
        '''Funcion que produce desviacion estandar global'''
        var = []
        for i,e in enumerate(semanas): var.append(semanas[e])
        s = stats(var)
        s = s.desviacion()
        return s


if __name__ == '__main__':
    folder = sys.argv[1]
    valor = ["valorDemanda","valorGeneracion","valorPronostico"]
    a = Analisis(folder)
    for i,e in enumerate(valor):
        mediaPorDia = a.mediaPorDia(e)[0]
        mediaPorSemana = a.mediaPorDia(e)[1]
        print colored("Media Aritmetica Diaria ",attrs=['bold']),e
        for i in range(1,6):
            print colored("semana%d"%i,"magenta", attrs=['bold'])
            print colored(mediaPorDia["semana%d"%i],"magenta")
            print " "
        print " "
        print colored("Media Aritmetica Semanal ",attrs=['bold']),e
        for e in mediaPorSemana:
            print colored(e,"cyan",attrs=['bold'])
            print colored(mediaPorSemana[e],"cyan")
        print " "
    #s = a.desviacionPorSemana(m)
    #a.diaspico()
    #v = a.desviacionSemanal(s)
    p.removeALL(p.extractAll(folder))
    driver = webdriver.Firefox()

    page = "http://lexielexter.96.lt/"
    driver.get(page)
