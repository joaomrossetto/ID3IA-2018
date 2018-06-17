from __future__ import division
import pandas as pd
import numpy as np
import calcEntropy as calc
import arvoreDecisao as decisao

adults = pd.read_csv('adult_dataprep.data.txt', sep=',', header = None)
adults = adults.values
#indiceDoAtributo = calc.getIndiceAtributo(jogaTenis, 'temp')
#print(indiceDoAtributo)
#arvore = Tree.Arvore()

Root = decisao.ArvoreDecisao(adults,'X50k.year', adults[0], 0)
#decisao.display(Root)
print(Root.filhos)
decisao.classificador(adults, Root)

#arvore.display("relationship")
#print(calc.makeConjuntoAtributo(jogaTenis,"outlook","Overcast"))
#print(calc.getProporcaoPositiva(calc.makeConjuntoAtributo(jogaTenis,"outlook","Rain")))
#print(calc.getProporcaoNegativa(calc.makeConjuntoAtributo(jogaTenis,"outlook","Rain")))
#valoresAtributo = calc.getValoresAtributos(jogaTenis,"temp")
#print(valoresAtributo[0])
#calc.calculaGanhoInformacao(jogaTenis,"outlook")
#calc.calculaGanhoInformacao(jogaTenis,"temp")
#calc.calculaGanhoInformacao(jogaTenis,"humidity")
#calc.calculaGanhoInformacao(jogaTenis,"wind")

