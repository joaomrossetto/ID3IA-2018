from __future__ import division
import pandas as pd
import arvoreDecisao as decisao


def imprime(Root, caminho, rules,contador):
    if Root =='<=50K' or Root ==">50K":
      contador[0] = contador[0] + 1
      teste = ""
      for a in rules:
         teste= teste + a  + " "
      teste = teste + 'THEN: '+Root
      caminho.append(teste) 
    else:
        if len(rules) == 0:
           x='IF '
        else:
           x='AND '
        rules.append(x + "|" + Root.atributo + "|" )
        contador[1] = contador[1] + 1
        filho = Root.filhos
        for f in filho:
            rules.append(' = ' + f)
            imprime(filho[f], caminho, rules,contador)
            rules.pop(len(rules)-1)
        rules.pop(len(rules)-1)

Adults = pd.read_csv('adult_dataprep.data.txt', sep=',', header = None)
Adults = Adults.values
#indiceDoAtributo = calc.getIndiceAtributo(Tenis, 'temp')
#print(indiceDoAtributo)
#arvore = Tree.Arvore()

Root = decisao.ArvoreDecisao(Adults,'X50k.year', Adults[0], 0)
#decisao.display(Root)
#decisao.display(Root,"",caminho)
caminho = []
rules = []
contador=[0,0]
imprime(Root,caminho,rules, contador)
for i in caminho:
    print(i)
decisao.classificador(Adults, Root)
Root= decisao.poda2(Root,Adults) 

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

