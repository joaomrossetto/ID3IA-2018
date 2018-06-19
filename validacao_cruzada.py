from __future__ import division
import pandas as pd 
import numpy as np
import arvoreDecisao as decisao
import math as mt

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
        train_set.to_csv('adult_train_set.data.txt', sep=',', index=False)
        treinamento = pd.read_csv('adult_train_set.data.txt', sep=',', header = None)
        treinamento = treinamento.values
        arvore = decisao.ArvoreDecisao(treinamento,'X50k.year', treinamento[0], 0)
        teste = pd.read_csv('adult_test_set.data.txt', sep=',', header = None)
        teste = teste.values
        lista_erros.append(1-(decisao.classificador(teste, arvore)))
    soma_erros = 0.0
    erros_file = open("erros_{}_folds.txt".format(k), 'w')
    for j in lista_erros:
        erros_file.write("%f " % j)
        soma_erros += j
    media_erros = soma_erros / k  
    return media_erros

def erroVerdadeiro(erroMedio, totaldeExemplos):
    aux = round(erroMedio*(1-erroMedio),6)
    erroPadrao = round(mt.sqrt(aux/totaldeExemplos),6)
    aux2 = round(1.96*erroPadrao,6)
    limiteInferior = erroMedio - aux2
    limiteSuperior = erroMedio + aux2
    intervalo = (str(limiteInferior) + "-" + str(limiteSuperior))
    print('O erro verdadeiro fica entre: ', limiteInferior , ' e ', limiteSuperior)
    return intervalo


adults = pd.read_csv('adult_dataprep.data.txt', sep=r'\s*,\s*', na_values="?", engine='python')
adults_tam = len(adults)
folds = cria_folds(adults,10)
media_erros = validacao_cruzada(folds)
print('A media dos erros foi de: %f' % media_erros)
intervalo = erroVerdadeiro(media_erros,adults_tam)
erro_vdd_file = open("true_error_{}_folds.txt".format(len(folds)), 'w')
erro_vdd_file.write("%s" % intervalo)