from stats import Estadisticas as stats
import data
import sys
import datetime
import pickle
from termcolor import colored
import pandas
p = data.Pandax()

prueba = [10, 18, 15, 12, 3, 6, 5, 7]
def horapico(folder):
    semanas = p.get_weeks(p.extractAll(folder))
    ds = []
    cont = 0
    results = {}
    folder = sys.argv[1]
    horapico =  p.jsontopanda("horapico.json")["valorDemanda"].astype(int)
    dias =  p.jsontopanda("horapico.json")["dias"].astype(int)
    semanas = p.get_weeks(p.extractAll(folder))
    for element in semanas:
        pandax = []
        ds = []
        for i in range(len(semanas[element])):
            f = semanas[element][i]+".mexico.txt"
            try:
                horapico += p.jsontopanda(f)["valorDemanda"].astype(int) + horapico
            except ValueError:
                plo = p.jsontopanda(f)["valorDemanda"][:23].astype(int)
                horapico += horapico +  plo

            pandita = p.jsontopanda(f)["valorDemanda"].tolist()
            s = stats(pandita)
            s = s.desviacion()
            #desviacion stard semana demanda
            ds.append(s)
            pandax.append(p.jsontopanda(f))
        print ds
        results[element] = ds
    print "horapico :", colored(horapico.div(dias),"magenta")

    #for i in results: print results[i],i
    with open('results.pickle', 'wb') as handle:
        pickle.dump(results, handle)

if __name__ == '__main__':
    folder = sys.argv[1]

    horapico(folder)

    p.removeALL(p.extractAll(folder))
