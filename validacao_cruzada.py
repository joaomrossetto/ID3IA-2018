import pandas as pd 
import numpy as np
import arvoreDecisao as decisao

def cria_folds(dados, k):
    folds = []
    tam_base = len(dados)
    print('tam_base: %s \n' % tam_base)
    tam_fold = int(tam_base / k)
    print('tam_fold: %s \n' % tam_fold)
    for i in range(k):
        amostra = dados.sample(tam_fold)
        folds.append(amostra)
        print('Amostra: %s \n \n ' % amostra)
        print('Amostra.index: %s \n \n' % amostra.index)
        print(i)
        for row in amostra.itertuples():
            dados.drop(row.Index, inplace=True)
    print('\nlen(dados): %d\n' % len(dados))
    if len(dados) != 0:
        folds[0].append(dados)
    print(type(folds))
    print(folds)
    return folds

def validacao_cruzada(folds):
    lista_erros = []
    k = (len(folds))
    for i in range(k):
        test_set = folds[i]
        print(type(test_set))
        print(test_set)
        test_set.to_csv('adult_test_set.data.txt', sep=',', index=False)
        train_set = pd.concat((folds[:i]+folds[i+1:]))
        print(type(train_set))
        print(train_set)
        #folds[:i] + folds[i+1:]
        #train_set = train_set.values
        #treinamento = train_set.iloc[0]
        #train_set = train_set.as_matrix(treinamento)
        #print(type(train_set))
        #print(train_set)
        train_set.to_csv('adult_train_set.data.txt', sep=',', index=False)
        treinamento = pd.read_csv('adult_train_set.data.txt', sep=',', header = None)
        treinamento = treinamento.values
        arvore = decisao.ArvoreDecisao(treinamento,'X50k.year', treinamento[0], 0)
        teste = pd.read_csv('adult_test_set.data.txt', sep=',', header = None)
        teste = teste.values
        lista_erros.append(decisao.classificador(teste, arvore))
    soma_erros = 0.0
    for j in lista_erros:
        soma_erros += j
    media_erros = soma_erros / k  
    return media_erros

adults = pd.read_csv('adult_dataprep.data.txt', sep=r'\s*,\s*', na_values="?", engine='python')
folds = cria_folds(adults,4)
media_erros = validacao_cruzada(folds)