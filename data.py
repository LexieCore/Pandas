import sys
from termcolor import colored

usage = "python %s filename.zip"
if len(sys.argv) != 2:
    print >> sys.stderr, \
    "Debes introducir :  " + usage % sys.argv[0]
    sys.exit(1)

import os,pandas
import datetime
from zipfile import ZipFile as zip

archivoJSON = "all_data_sin.json"
class Pandax:


    def extractAll(self,zipName):
        '''Extrae el contenido del archivo .zip; produce una lista que contiene los nombres de todos los archivos'''
        z = zip(zipName)
        files = []
        for i,f in enumerate(z.namelist()):
            files.append(f)
            if f.endswith('/'):
                os.makedirs(f)
                z.extract(f)
            z.extract(f)
        return files

    def jsontopandaS(self,files):
        '''Lee archivos tipo .json; produce pandas dataframes por cada archivo'''
        for f in files:
            print str(pandas.read_json(path_or_buf=f))


    def pandastopanda(self,pandax,nombre):
        '''Recibe pandas dataframes, los mezcla en uno solo y almacena el resultado en un archivo llamado all_data_sin.json'''
        frames = [ pandas.read_json(path_or_buf=panda) for panda in pandax ]
        result = pandas.concat(frames)
        result.reset_index().to_json(path_or_buf=nombre,orient='records')
        return results

    def jsontopanda(self,archivoJSON,columna):
        '''Imprime en consola el panda dataframe contenido en un archivo .json'''
        return pandas.read_json(path_or_buf=archivoJSON)[columna]

    def removeALL(self,files):
        '''Recibe una lista con nombres de archivos y los elimina; Elimina todos los archivos que fueron extraidos del archivo .zip'''
        for f in files:
            os.remove(f)
        print colored("fin","red")
    def get_columns():
        df = DataFrame(randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])

    def get_weeks(self,files):
        '''Recibe una lista de nombres de archivos .json y agrupa los dias en semanas iniciando por la fecha mas baja'''
        fechas = []
        for f in files:
            fecha = f[:10]
            fecha = fecha.replace(".", "")
            fechas.append(datetime.datetime.strptime(fecha, "%d%m%Y").date())
        fechas = sorted(fechas)
        semanas = {}
        semana = []
        e = 1
        while fechas:
            for i in range(7):
                try:
                    semana.append(fechas.pop(0))
                except IndexError:
                    break
            semanas["semana%s"%e] = semana
            semana = []
            e+=1
        fechas = {}
        for element in semanas:
            temp = []
            for i in range(len(semanas[element])):
                temp.append(datetime.datetime.strftime(semanas[element][i],"%d-%m-%Y").replace("-","."))
            fechas[element] = temp
        return fechas


if __name__ == '__main__':
    p = Pandax()
    demanda = p.jsontopanda("11.04.2016.mexico.txt","valorDemanda")
    for i,e in enumerate(demanda):
        print e + "+", ":D"
