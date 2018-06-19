from __future__ import division
import pandas as pd 
import numpy as np

def limpa_base():
    adults = pd.read_csv('adult_discretizado.data.txt', sep=r'\s*,\s*', na_values="?", engine='python')
    print(adults)
    print('Tamanho inicial da base: %d \n' % len(adults))
    adults.dropna(how='any',inplace = True)
    adults = adults.reset_index(drop=True)
    print('Tamanho apos limpeza: %d \n' % len(adults))
    print(adults)
    adults.to_csv('adult_dataprep.data.txt', sep=',', index=False)
    return adults


base = limpa_base()




