from __future__ import division
import pandas as pd
import arvoreDecisao as decisao

Adults = pd.read_csv('adult_dataprep.data.txt', sep=',', header = None)
Adults = Adults.values
#indiceDoAtributo = calc.getIndiceAtributo(Tenis, 'temp')
#print(indiceDoAtributo)
#arvore = Tree.Arvore()

Root = decisao.ArvoreDecisao(Adults,'X50k.year', Adults[0], 0)
#decisao.display(Root)
print(Root.atributo)
print(Root.filhos)
decisao.classificador(Adults, Root)

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

