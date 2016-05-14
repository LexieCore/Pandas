import sys
import termcolor
usage = "python %s filename.zip"
if len(sys.argv) != 2:
    print >> sys.stderr, \
    colored("Debes introducir :  " + usage % sys.argv[0],"yellow")
    sys.exit(1)

import os,pandas
from zipfile import ZipFile as zip

archivoJSON = "all_data_sin.json"

def extractAll(zipName):
    '''Extrae el contenido del archivo .zip; produce una lista que contiene los nombres de todos los archivos'''
    z = zip(zipName)
    files = []
    for f in z.namelist():
        files.append(f)
        if f.endswith('/'):
            os.makedirs(f)
        else:
            z.extract(f)
    return files

def jstopandaS(files):
    '''Lee archivos tipo .json; produce pandas dataframes por cada archivo'''
    for f in files:
        print str((pandas.read_json(path_or_buf=f)))

def pandastopanda(pandax):
    '''Recibe pandas dataframes, los mezcla en uno solo y almacena el resultado en un archivo llamado all_data_sin.json'''
    frames = [ pandas.read_json(path_or_buf=panda) for panda in pandax ]
    result = pandas.concat(frames)
    result.reset_index().to_json(path_or_buf="all_data_sin.json",orient='records')

def jsontopanda(archivoJSON):
    '''Imprime en consola el panda dataframe contenido en un archivo .json'''
    print pandas.read_json(path_or_buf=archivoJSON)

def removeALL(files):
    '''Recibe una lista con nombres de archivos y los elimina; Elimina todos los archivos que fueron extraidos del archivo .zip'''
    for f in files:
        os.remove(f)
    print "removed"

files = extractAll(sys.argv[1])
#jstopandaS(files)
pandastopanda(files)
jsontopanda(archivoJSON)
removeALL(files)
