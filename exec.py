from __future__ import division
import pandas as pd
import arvoreDecisao as decisao
import validacao_cruzada as vc

#Adults = pd.read_csv('adult_dataprep.data.txt', sep=r'\s*,\s*', na_values="?", engine='python')
Adults = pd.read_csv('adult_dataprep.data.txt', sep=',')
CjID3 = vc.cria_folds(Adults,3)
treino = CjID3[0]
treino.to_csv('cjid3_0.txt', sep=',', index=False)
teste = CjID3[1]
teste.to_csv('cjid3_1.txt', sep=',', index=False)
valida = CjID3[2]
valida.to_csv('cjid3_2.txt', sep=',', index=False)
#CjID3[0] = CjID3[0].values #Treino
#CjID3[1] = CjID3[1].values #Teste
#CjID3[2] = CjID3[2].values #Validacao

#Adults = pd.read_csv('adult_dataprep.data.txt', sep=',')
#crossVal = vc.cria_folds(Adults, 10)
#mediaErros = vc.validacao_cruzada(crossVal)

treinamento = pd.read_csv('cjid3_0.txt', sep=',', header = None)
treinamento = treinamento.values
Root = decisao.ArvoreDecisao(treinamento,'X50k.year',treinamento[0],0)
#print(decisao.classificador(CjID3[1], Root))
caminho = []
rules = []
contador = [0,0]
#decisao.imprime(Root, caminho, rules, contador)
#decisao.poda1(Root,CjID3[2])
validacao = pd.read_csv('cjid3_2.txt', sep=',', header = None)
validacao = validacao.values
Root = decisao.poda2(Root,Root,validacao,0)

test = pd.read_csv('cjid3_1.txt', sep=',', header = None)
test = test.values
print(decisao.classificador(teste, Root))
