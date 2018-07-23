from __future__ import division
import pandas as pd
import arvoreDecisao as decisao
import validacao_cruzada as vc

teste = pd.read_csv('cjid3_0.txt', sep=',', header = None)
treino = pd.read_csv('cjid3_1.txt', sep=',', header = None)
treino = treino.values
teste = teste.values

Root = decisao.ArvoreDecisao(treino,'X50k.year',treino[0],0)
caminho = []
rules = []
contador = [0,0]
decisao.getCaminhosMaisUsados(teste, Root)
decisao.imprime(Root,caminho,rules,contador)
print(caminho)

#print(listaRegras)
