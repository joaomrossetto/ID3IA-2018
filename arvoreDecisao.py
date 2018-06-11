from __future__ import division
import math as mt
import numpy as np
import copy as cp
import calcEntropy as calc
from anytree import Node, RenderTree

def ValorMaisComum(Dados, Target, Atributos):
	MaisComum = ''
	ganhaMais = calc.getNumeroAparicoes(Dados, Target, ">50K")	
	ganhaMenos = calc.getNumeroAparicoes(Dados, Target, "<=50K")
	if ganhaMais > ganhaMenos:
		MaisComum = '>50K'
	else:
 		MaisComum = '<=50K'
	return MaisComum


def MelhorAtributo (Dados, Target, Atributos):
	Melhor = Atributos[0]
	Ganho = 0
	numAtributos = len(Atributos)
	for i in range(0, numAtributos):
		NovoGanho = calc.calculaGanhoInformacao(Dados, Target)
		if NovoGanho > Ganho:
			Ganho = NovoGanho
			Melhor = Atributos[i]
	return Melhor

def Excluir_vetor(vetor,atributo):
    tam = len(vetor)
    novoconjunto = []
    for i in range(0, tam):
        if vetor[i] != atributo:
            novoconjunto.append(vetor[i])
    return novoconjunto



def ArvoreDecisao(Dados, Target, Atributos):
	indice = calc.getIndiceAtributo(Dados,Target)
	maior = "Yes"
	menor = "No"
	imaior = 0
	imenor = 0
	a = ""
	for i in range (0,len(Dados)):
		if imaior > 0 and imenor > 0:
			break
		elif Dados[i][indice] == maior:
			imaior = imaior + 1
		elif Dados[i][indice] == menor:
			imenor = imenor + 1
	#### se tudo for igual 
	if imenor == len(Dados):
		return maior
	elif imaior == len(Dados):
		return menor

	##se acabarem os atributos
	if len(Atributos) == 0:
		return ValorMaisComum(Dados,Target,Atributos)
	else: 
		a = MelhorAtributo(Dados, Target, Atributos)
		Root = Node(a)

	Valores_A = calc.getValoresAtributos(Dados,a)
	#for ind in range(0,len(Atributos)):
	#	if Atributos[ind]==a:
	#		break

	Subconjunto=[]

	for y in range (0,len(Valores_A)):
		Subconjunto = calc.makeConjuntoAtributo(Dados,a,Valores_A[y])
		if len(Subconjunto) == 0:
			No = Node(ValorMaisComum(Dados,Target,Atributos), parent=Root)
		else:

			ArvoreDecisao(Subconjunto,Target,Excluir_vetor(Atributos,a))

	return No 



	
