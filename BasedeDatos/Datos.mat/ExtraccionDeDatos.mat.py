# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 20:07:20 2024

@author: Fausto
"""
import numpy as np
import pandas as pd
from pymatreader import read_mat

data = read_mat('507_Depression_REST.mat')
rawdata = data['EEG']['data']

rawdatatranspuesta = np.transpose(rawdata)

df = pd.DataFrame(rawdatatranspuesta)

#Genera un archivo .csv
df.to_csv('raw_data.csv', index=False)
