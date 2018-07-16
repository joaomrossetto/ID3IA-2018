from __future__ import division
import pandas as pd
import arvoreDecisao as decisao
import validacao_cruzada as vc

colunas = ['age','workclass','education','education.num','marital.status','occupation','relationship',
'race','sex','capital.gain','capital.loss','hours.per.week','native.country','X50k.year']

Adults = pd.read_csv('adult_dataprep.data.txt', sep=r'\s*,\s*', na_values="?", engine='python',header=0)
print(type(Adults))
print(Adults.head())
print(Adults.iloc[0,:])
CjID3 = vc.cria_folds(Adults,3)
CjID3[0] = CjID3[0].values #Treino
CjID3[1] = CjID3[1].values #Teste
CjID3[2] = CjID3[2].values #Validacao
Adults = pd.read_csv('adult_dataprep.data.txt', sep=r'\s*,\s*', na_values="?", engine='python',header=0)
crossVal = vc.cria_folds(Adults, 10)
mediaErros = vc.validacao_cruzada(crossVal)
Root = decisao.ArvoreDecisao(CjID3[0],'X50k.year', colunas ,"")
print(decisao.classificador(CjID3[1], Root))
caminho = []
rules = []
contador = [0,0]
decisao.imprime(Root, caminho, rules, contador)
decisao.poda1(Root,CjID3[2])
decisao.poda2(Root,CjID3[2])
print(decisao.classificador(CjID3[1], Root))
