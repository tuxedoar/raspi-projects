#!/usr/bin/env python
# Lee datos recabados del archivo CSV y grafica la evolucion de la temperatura. Requiere matplotlib!.
# Given a CSV file with temperatures and date/time records, it generates a graph. It requires matplotlib!. 
import re
from datetime import datetime
from matplotlib import pyplot as plt
from matplotlib import dates
import sys, argparse

x =[]
y =[]
listatemp = []

labels=''
archivo_csv = ''
titulo = 'SIN TITULO'
exportar = False

def LeerCSV(archivo_csv):
        global labels
        try:
                archivo = open(archivo_csv, 'r')
        except:
                print "El archivo indicado NO existe!."
                sys.exit(2)
        
        for linea in archivo.readlines():
        # Busco las etiquetas para los ejes X e Y ; Si las encuentro, las almaceno en variable labels
                title = re.match("[a-zA-Z\;a-zA-z]", linea)
                if title:
                        labels = linea
                        # Divido la lista con las etiquetas.
                        labels = labels.split(";")
                        continue
                # Separo hora y temperatura
                linea = linea.strip()
                item = linea.split(",")
                # Crea una lista por valor de hora y temp!
                listatemp.append(item)
        archivo.close()

def graficarGUI(titulo):
        # Elimino la 1er lista que contiene un '\n'
        del listatemp[0]
        # De la lista temporal, lleno las listas x, y con hora y temperatura
        for elemento in listatemp:
                elemento[0] = datetime.strptime(elemento[0], "%d-%m-%Y %H:%M:%S")
                x.append(elemento[0])
                y.append(elemento[1])
        
        xs = dates.date2num(x)
        hfmt = dates.DateFormatter('%d-%m-%Y\n%H:%M:%S')

        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)

        # Asigno cada etiqueta.
        ax.set_xlabel(labels[0])
        ax.set_ylabel(labels[1])

        ax.xaxis.set_major_formatter(hfmt)
        # Elijo cuantos valores quiero en el eje X e Y.
        ax.locator_params(axis='x',nbins=3)
        ax.locator_params(axis='y',nbins=5)

        ax.set_title(titulo)
        ax.grid(True)
        ax.plot(xs, y)

        # Exporto la grafica a imagen o la muestro en la GUI.
        if exportar != False:
                plt.savefig(exportar)
        else:
                plt.show()

parser = argparse.ArgumentParser(description='Graficar valores en archivo CSV')

parser.add_argument('-f','--file', help='Indica el archivo CSV a graficar', required=True)
parser.add_argument('-t','--title', help='Asigna un titulo a la grafica', default=titulo, required=False)
parser.add_argument('-e','--export', help='Exporta la imagen a un archivo', default=exportar, required=False)

args = parser.parse_args()

archivo_csv = args.file
titulo = args.title
exportar = args.export

LeerCSV(archivo_csv)
graficarGUI(titulo)
