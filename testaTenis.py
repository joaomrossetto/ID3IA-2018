from __future__ import division
import pandas as pd
import numpy as np
import calcEntropy as calc
jogaTenis = pd.read_csv('playtennis.csv', sep=',', header = None)
jogaTenis = jogaTenis.values
print(jogaTenis)
indiceDoAtributo = calc.getIndiceAtributo(jogaTenis, 'temp')
print(indiceDoAtributo)
#print(calc.makeConjuntoAtributo(jogaTenis,"outlook","Overcast"))
print(calc.getProporcaoPositiva(calc.makeConjuntoAtributo(jogaTenis,"outlook","Rain")))
print(calc.getProporcaoNegativa(calc.makeConjuntoAtributo(jogaTenis,"outlook","Rain")))
#valoresAtributo = calc.getValoresAtributos(jogaTenis,"temp")
#print(valoresAtributo[0])
calc.calculaGanhoInformacao(jogaTenis,"outlook")