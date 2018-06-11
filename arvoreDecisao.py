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


def MelhorAtributo (Dados,Atributos):
	Melhor = Atributos[0]
	Ganho = 0
	numAtributos = len(Atributos) -1 
	for i in range(0, numAtributos):
		if i==0:
		   Ganho = calc.calculaGanhoInformacao(Dados, Atributos[i])
		NovoGanho = calc.calculaGanhoInformacao(Dados, Atributos[i])
		print(Atributos[i])
		print(NovoGanho)
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
	for i in range (1,len(Dados)):
		if imaior > 0 and imenor > 0:
			break
		elif Dados[i][indice] == maior:
			imaior = imaior + 1
		elif Dados[i][indice] == menor:
			imenor = imenor + 1
	#### se tudo for igual 
	if imenor == len(Dados) -1 :
		print(menor)
		return menor
	elif imaior == len(Dados) -1:
		print(maior)
		return maior

	##se acabarem os atributos
	if len(Atributos) == 1:
		return ValorMaisComum(Dados,Target,Atributos)
	else: 
		a = MelhorAtributo(Dados,Atributos)
		Root = Node(a)
		print("Atributo: " + a)
		Valores_A = calc.getValoresAtributos(Dados,a)
	#for ind in range(0,len(Atributos)):
	#	if Atributos[ind]==a:
	#		break

		

		for y in range (0,len(Valores_A)):
			Subconjunto=[]
			Subconjunto = calc.makeConjuntoAtributo(Dados,a,Valores_A[y])
			print("Valor: " +Valores_A[y])
			if len(Subconjunto) == 1:
				x = Node(ValorMaisComum(Dados,Target,Atributos), parent=Root)
				print(ValorMaisComum(Dados,Target,Atributos))
			else:
				x = Node(ArvoreDecisao(Subconjunto,Target,Excluir_vetor(Atributos,a)), parent=Root)
	    
	return Node 



	
