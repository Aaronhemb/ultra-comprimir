# -*- coding: utf-8 -*-
"""
Created on Mon Mar  6 13:48:51 2023

@author: oax_r
"""


""" Arvhivo original

import py7zr
import os
import datetime

def comprimir_carpeta(carpetapath, archivopath):
    fecha_hora = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    archivoname = os.path.basename(carpetapath) + '_' + fecha_hora + '.7z'
    archivopath = os.path.join(os.path.dirname(archivopath), archivoname)
    with py7zr.SevenZipFile(archivopath, 'w') as zip:
        for root, dirs, files in os.walk(carpetapath):
            for file in files:
                zip.write(os.path.join(root, file), file)

carpetapath = './DOCUMENTOS/'
archivopath = './RESULTADO/carpeta.7z'

comprimir_carpeta(carpetapath, archivopath)

"""
"""
Archivo complemento comprimido ultra  


   
import py7zr
import os
import shutil
import datetime

def comprimir_carpeta(carpetapath, archivopath):
    fecha_hora = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    archivoname = os.path.basename('respaldo') + '_' + fecha_hora + '.7z'
    archivopath = os.path.join(os.path.dirname(archivopath), archivoname)
    with py7zr.SevenZipFile(archivopath, 'w') as zip:
        for root, dirs, files in os.walk(carpetapath):
            for file in files:
                zip.write(os.path.join(root, file), file)
    for root, dirs, files in os.walk(carpetapath):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            shutil.rmtree(os.path.join(root, dir))

carpetapath = './DOCUMENTOS/'
archivopath = './RESULTADO/carpeta.7z'

comprimir_carpeta(carpetapath, archivopath)

 
   
  

import os
import shutil
import datetime
import py7zr

def comprimir_carpeta(carpetapath, archivopath):
    fecha_hora = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    archivoname = os.path.basename('respaldo') + '_' + fecha_hora + '.7z'
    archivopath = os.path.join(archivopath, archivoname)
    with py7zr.SevenZipFile(archivopath, 'w') as zip:
        for root, dirs, files in os.walk(carpetapath):
            for file in files:
                zip.write(os.path.join(root, file), file)
    for root, dirs, files in os.walk(carpetapath):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            shutil.rmtree(os.path.join(root, dir))

carpetapath = input("Ingrese la ruta de la carpeta que desea comprimir: ")
archivopath = input("Ingrese la ruta de la carpeta donde desea guardar el archivo comprimido: ")

comprimir_carpeta(carpetapath, archivopath)

"""      

import os
import shutil
import datetime
import py7zr

def comprimir_carpeta(carpetas, archivopath):
    fecha_hora = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    for i, carpetapath in enumerate(carpetas):
        archivoname = os.path.basename(carpetapath) + '_' + fecha_hora + '_parte' + str(i+1) + '.7z'
        archivopath_i = os.path.join(archivopath, archivoname)
        with py7zr.SevenZipFile(archivopath_i, 'w') as zip:
            for root, dirs, files in os.walk(carpetapath):
                for file in files:
                    zip.write(os.path.join(root, file), file)
        for root, dirs, files in os.walk(carpetapath):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                shutil.rmtree(os.path.join(root, dir))

# Seleccionar la carpeta de origen
print('Seleccione la carpeta de origen:')
carpetapath = input()

# Seleccionar la carpeta de destino
print('Seleccione la carpeta de destino:')
archivopath = input()

# Obtener la lista de subcarpetas dentro de la carpeta de origen
carpetas = [os.path.join(carpetapath, carpeta) for carpeta in os.listdir(carpetapath) if os.path.isdir(os.path.join(carpetapath, carpeta))]

# Comprimir cada subcarpeta en un archivo 7z separado
comprimir_carpeta(carpetas, archivopath)






