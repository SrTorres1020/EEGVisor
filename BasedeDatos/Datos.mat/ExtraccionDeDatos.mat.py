# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 20:07:20 2024

@author: Fausto
"""
import numpy as np
import pandas as pd
from pymatreader import read_mat

data = read_mat('C:\\Users\\Fausto\\Documents\\github\\Archivos\\EEG_Depression\\507_Depression_REST.mat')
df = pd.DataFrame(np.transpose(data['EEG']['data']))

# #Genera un archivo .csv
df.to_csv('C:\\Users\\Fausto\\Documents\\github\\Archivos\\EEG_Depression\\raw_data.csv', index=False)

