import pandas as pd
import numpy as np
import calcEntropy as calc
jogaTenis = pd.read_csv('playtennis.csv', sep=',', header = None)
jogaTenis = jogaTenis.values
print(jogaTenis)
indiceDoAtributo = calc.getIndiceAtributo(jogaTenis, 'temp')
print(indiceDoAtributo)
print(calc.getProporcaoPositiva(jogaTenis))
print(calc.getProporcaoNegativa(jogaTenis))
print(calc.calculaEntropy(jogaTenis))
valoresAtributo = calc.getValoresAtributos(jogaTenis,"temp")
print(valoresAtributo[0])
calc.calculaGanhoInformacao(jogaTenis)
