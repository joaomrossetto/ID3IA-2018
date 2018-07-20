from __future__ import division
import pandas as pd 
import numpy as np
import arvoreDecisao as decisao
import math as mt
import matplotlib.pyplot as plt

def cria_folds(dados, k):
    folds = []
    tam_base = len(dados)
    print('tam_base: %s \n' % tam_base)
    tam_fold = int(tam_base / k)
    print('tam_fold: %s \n' % tam_fold)
    for i in range(k):
        amostra = dados.sample(tam_fold)
        folds.append(amostra)
        #print('Amostra: %s \n \n ' % amostra)
        #print('Amostra.index: %s \n \n' % amostra.index)
        #print(i)
        for row in amostra.itertuples():
            dados.drop(row.Index, inplace=True)
    #print('\nlen(dados): %d\n' % len(dados))
    if len(dados) != 0:
        folds[0].append(dados)
    #print(type(folds))
    #print(folds)
    return folds

def validacao_cruzada(folds):
    lista_erros = []
    k = (len(folds))
    for i in range(k):
        test_set = folds[i]
        test_set.to_csv('adult_test_set.data.txt', sep=',', index=False)
        train_set = pd.concat((folds[:i]+folds[i+1:]))
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

'''
adults = pd.read_csv('adult_dataprep.data.txt', sep=r'\s*,\s*', na_values="?", engine='python')
adults_tam = len(adults)
folds = cria_folds(adults,10)
media_erros = validacao_cruzada(folds)
print('A media dos erros foi de: %f' % media_erros)
intervalo = erroVerdadeiro(media_erros,adults_tam)
erro_vdd_file = open("true_error_{}_folds.txt".format(len(folds)), 'w')
erro_vdd_file.write("%s" % intervalo)

#erros = pd.read_csv('erros_10_folds.txt')
erros10 = [0.177719, 0.160146, 0.169098, 0.165782, 0.155836, 0.170756, 0.178050, 0.180371, 0.170093, 0.159814 ]
erros9 = [0.167413, 0.163533, 0.165622, 0.175768, 0.176664, 0.150701, 0.164429, 0.163533, 0.174276 ]
erros8 = [0.183024, 0.165252, 0.162865, 0.169496, 0.177454, 0.164191, 0.172414, 0.164721 ]
erros7 = [0.160631, 0.169684, 0.163649, 0.165506, 0.171309, 0.166667, 0.163417 ]
erros6 = [0.168291, 0.168092, 0.177442, 0.162522, 0.166302, 0.169286]
erros5 = [0.161638, 0.168932, 0.168435, 0.181698, 0.172745]
# basic plot
data = [erros5, erros6, erros7, erros8, erros9,erros10]
fig, ax1 = plt.subplots(figsize=(10, 6))
fig.canvas.set_window_title('A Boxplot Example')
plt.boxplot(data)
plt.xticks([1, 2, 3, 4, 5, 6], [5, 6, 7, 8, 9, 10])
ax1.set_title('Erros do modelo por K em K-Fold')
ax1.set_xlabel('Valor de K')
ax1.set_ylabel('Erro')
plt.show()
'''