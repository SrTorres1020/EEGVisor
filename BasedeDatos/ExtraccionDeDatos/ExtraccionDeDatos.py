# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 16:49:16 2024

@author: Fausto
"""

import wx
import numpy as np
import pandas as pd
import mne
from pymatreader import read_mat

def abrir_archivo():
    # Crear una instancia de la aplicación
    app = wx.App(False)
    
    # Abrir un cuadro de diálogo para seleccionar un archivo
    cuadro_dialogo = wx.FileDialog(
        None, "Seleccionar archivo", wildcard="All Files (*.*)|*.*", 
        style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
    )
    
    if cuadro_dialogo.ShowModal() == wx.ID_OK:
        ruta_archivo = cuadro_dialogo.GetPath()
        print(f"Archivo seleccionado: {ruta_archivo}")
        
        # Determinar el tipo de archivo y llamar a la función de procesamiento correspondiente
        if ruta_archivo.lower().endswith('.edf'):
            procesar_archivo_edf(ruta_archivo)
        elif ruta_archivo.lower().endswith('.mat'):
            procesar_archivo_mat(ruta_archivo)

    # Limpiar
    cuadro_dialogo.Destroy()
    app.MainLoop()

def procesar_archivo_edf(ruta_archivo):
    # Cargar el archivo EDF
    raw = mne.io.read_raw_edf(ruta_archivo)
    
    # Extraer los datos crudos (voltajes) y transponer la matriz para exportar
    df = pd.DataFrame(np.transpose(raw.get_data()))
    
    # Generar un archivo CSV
    ruta_csv = 'datos_crudos_edf.csv'
    df.to_csv(ruta_csv, index=False)
    print(f"Datos guardados en {ruta_csv}")

def procesar_archivo_mat(ruta_archivo):
    # Cargar el archivo MAT
    data = read_mat(ruta_archivo)
    
    # Extraer los datos y transponer la matriz para exportar
    df = pd.DataFrame(np.transpose(data['EEG']['data']))
    
    # Generar un archivo CSV
    ruta_csv = 'datos_crudos_mat.csv'
    df.to_csv(ruta_csv, index=False)
    print(f"Datos guardados en {ruta_csv}")

if __name__ == "__main__":
    abrir_archivo()


