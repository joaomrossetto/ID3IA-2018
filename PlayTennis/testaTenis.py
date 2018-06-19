from __future__ import division
import pandas as pd
from PlayTennis import arvoreDecisaoPlayTennis as apt

Tenis = pd.read_csv('playtennis.csv', sep=',', header = None)
Tenis = Tenis.values
#indiceDoAtributo = calc.getIndiceAtributo(Tenis, 'temp')
#print(indiceDoAtributo)
#arvore = Tree.Arvore()

Root = apt.ArvoreDecisao(Tenis,'play', Tenis[0], 0)
#decisao.display(Root)
print(Root.atributo)
print(Root.filhos)
apt.classificador(Tenis, Root)

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

