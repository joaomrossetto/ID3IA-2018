from __future__ import division
import pandas as pd
import numpy as np
import calcEntropy as calc


jogaTenis = pd.read_csv('playtennis.csv', sep=',', header = None)
jogaTenis = jogaTenis.values
print(jogaTenis)
indiceDoAtributo = calc.getIndiceAtributo(jogaTenis, 'temp')
print(indiceDoAtributo)
<<<<<<< HEAD
print(calc.getProporcaoPositiva(jogaTenis))
print(calc.getProporcaoNegativa(jogaTenis))
print(calc.calculaEntropy(jogaTenis))
valoresAtributo = calc.getValoresAtributos(jogaTenis,"temp")
print(valoresAtributo[0])
ganho = calc.calculaGanhoInformacao(jogaTenis)
print(ganho)
=======
#print(calc.makeConjuntoAtributo(jogaTenis,"outlook","Overcast"))
print(calc.getProporcaoPositiva(calc.makeConjuntoAtributo(jogaTenis,"outlook","Rain")))
print(calc.getProporcaoNegativa(calc.makeConjuntoAtributo(jogaTenis,"outlook","Rain")))
#valoresAtributo = calc.getValoresAtributos(jogaTenis,"temp")
#print(valoresAtributo[0])
calc.calculaGanhoInformacao(jogaTenis,"outlook")
>>>>>>> a06e1e08255141f49d868f7e3522081bb197b8ff
