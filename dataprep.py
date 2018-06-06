from __future__ import division
import pandas as pd 
import numpy as np

from random import sample

def limpa_base():
    adults = pd.read_csv('adult.data.txt', sep=r'\s*,\s*', na_values="?", engine='python', names = ['age',
    'workclass',
    'fnlwgt',
    'education',
    'education-num',
    'marital-status',
    'occupation',
    'relationship',
    'race',
    'sex',
    'capital-gain',
    'capital-loss',
    'hours-per-week',
    'native-country',
    '50k-year'])

    adults.dropna(how='any',inplace = True)
    print adults
    return adults
    #print(adults.isnull().sum())

def cria_folds(dados, k):
    folds = []
    tam_base = len(dados)
    print('tam_base: %s \n' % tam_base)
    tam_fold = int(tam_base / k)
    print('tam_fold: %s \n' % tam_fold)
    for i in range(k):
        amostra = dados.sample(tam_fold)
        folds.append(amostra)
        print('%s \n' % amostra)
        print('%s \n' % amostra.index)
        print(i)
        for row in amostra.itertuples():
            #print(row)
            dados.drop(row.Index, inplace=True)
    print('\nlen(dados): %d\n' % len(dados))
    if len(dados) != 0:
        #for linha in range(len(dados)):
            #print('linha: %d \n' % linha)
        folds[0].append(dados)
    return folds

def validacao_cruzada(folds):
    lista_erros = []
    k = len(folds)
    for i in range(k):
        test_set = folds[i]
        train_set = folds[:i] + folds[i+1:]
        arvore = id3(train_set)
        lista_erros.append(testa(arvore, test_set))
    soma_erros = 0.0
    for j in lista_erros:
        soma_erros += j
    media_erros = soma_erros / k  
    return media_erros


base = limpa_base()
folds = cria_folds(base[:107],3)
print (folds)



