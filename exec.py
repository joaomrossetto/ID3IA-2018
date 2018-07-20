from __future__ import division
import pandas as pd
import arvoreDecisao as decisao
import validacao_cruzada as vc
import pickle 

#Adults = pd.read_csv('adult_dataprep.data.txt', sep=r'\s*,\s*', na_values="?", engine='python')
Adults = pd.read_csv('adult_dataprep.data.txt', sep=',')
CjID3 = vc.cria_folds(Adults,3)

treino = CjID3[0]
treino.to_csv('cjid3_0.txt', sep=',', index=False)

teste = CjID3[1]
teste.to_csv('cjid3_1.txt', sep=',', index=False)

valida = CjID3[2]
valida.to_csv('cjid3_2.txt', sep=',', index=False)

#Adults = pd.read_csv('adult_dataprep.data.txt', sep=',')
#crossVal = vc.cria_folds(Adults, 10)
#mediaErros = vc.validacao_cruzada(crossVal)

treinamento = pd.read_csv('cjid3_0.txt', sep=',', header = None)
treinamento = treinamento.values

Root = decisao.ArvoreDecisao(treinamento,'X50k.year',treinamento[0],0)
#print("num_nos:", num_nos)

#num_nos_file = open('num_nos.txt', 'wb')
#pickle.dump(num_nos, num_nos_file)
#num_nos_file.close()


root_train_file = open(r'root_train.pkl','wb')
pickle.dump(Root,root_train_file)
root_train_file.close()

caminho = []
rules = []
contador = [0,0]

validacao = pd.read_csv('cjid3_2.txt', sep=',', header = None)
validacao = validacao.values

test = pd.read_csv('cjid3_1.txt', sep=',', header = None)
test = test.values

acuracia_antes = decisao.classificador(test, Root)

Root, lista_acuracias = decisao.poda2(Root,Root,validacao,0)

with open('lista_acuracias.txt','wb') as lista_acuracias_file:
    for a in lista_acuracias:
        lista_acuracias_file.write(str(a)+'\n')


acuracia_depois = decisao.classificador(test, Root)

root_poda_file = open(r'root_poda.pkl','wb')
pickle.dump(Root,root_poda_file)
root_poda_file.close()

f1 = open('acuracia_pre_poda.txt', 'wb')
#f1.write(acuracia_antes)
pickle.dump(acuracia_antes, f1)
f1.close()

f2 = open('acuracia_pos_poda.txt', 'wb')
#f2.write(acuracia_depois)
pickle.dump(acuracia_depois, f2)
f2.close()





root_2_file = open(r'root_train.pkl','rb')
Root2 = pickle.load(root_2_file)
root_2_file.close()

Root2, lista_acuracias2 = decisao.poda2(Root2,Root2,test,0)

root_poda2_file = open(r'root_poda2.pkl','wb')
pickle.dump(Root2,root_poda2_file)
root_poda2_file.close()


with open('lista_acuracias_2.txt','wb') as lista_acuracias_2_file:
    for a in lista_acuracias2:
        lista_acuracias_2_file.write(str(a)+'\n')





root_3_file = open(r'root_train.pkl','rb')
Root3 = pickle.load(root_3_file)
root_3_file.close()

treinamento_poda = pd.read_csv('cjid3_0.txt', sep=',', header = None)
treinamento_poda = treinamento_poda.values

Root3, lista_acuracias3 = decisao.poda2(Root3,Root3,treinamento_poda,0)

root_poda3_file = open(r'root_poda3.pkl','wb')
pickle.dump(Root3,root_poda3_file)
root_poda3_file.close()


with open('lista_acuracias_3.txt','wb') as lista_acuracias_3_file:
    for a in lista_acuracias3:
        lista_acuracias_3_file.write(str(a)+'\n')




#print("Acuracia antes da poda: %f",  acuracia_antes)
#print("Acuracia depois da poda: %f",  acuracia_depois)