from __future__ import division
import pandas as pd
import arvoreDecisao as decisao
import validacao_cruzada as vc


treinamento = pd.read_csv('cjid3_0.txt', sep=',', header = None)
treinamento = treinamento.values
teste = pd.read_csv('cjid3_1.txt', sep=',', header = None)
teste = teste.values


Root = decisao.ArvoreDecisao(treinamento,'X50k.year',treinamento[0],0)
caminho = []
rules = []
contador = [0,0]
decisao.getCaminhosMaisUsados(treinamento, Root)
decisao.imprime(Root,caminho,rules,contador)
print(caminho)

#print(listaRegras)
