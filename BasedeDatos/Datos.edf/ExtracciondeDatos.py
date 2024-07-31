# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 15:13:37 2024

@author: Fausto
"""
import numpy as np
import pandas as pd
import mne

#Abrir el archivo .edf
file = "S001R01.edf"

#Extrae el raw data que corresponde a los voltajes y transpone la matriz para su exportacion a SQL
raw = mne.io.read_raw_edf('S001R01.edf')
df= pd.DataFrame(np.transpose(raw.get_data()))

#Genera un archivo .csv
df.to_csv('raw_data.csv', index=False)