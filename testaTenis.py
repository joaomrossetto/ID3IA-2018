from __future__ import division
import pandas as pd
import arvoreDecisao as decisao
import validacao_cruzada as vc

tenis = pd.read_csv('playtennis.csv', sep=',', header = None)
tenis = tenis.values
Root = decisao.ArvoreDecisao(tenis,'play',tenis[0],0)
caminho = []
rules = []
contador = [0,0]
decisao.imprime(Root,caminho,rules,contador)
print(caminho)
print('só pra debugar')
decisao.classificador(tenis, Root)
listaRegras = []
decisao.visitaPrintandoRegras(Root)
print(listaRegras)
