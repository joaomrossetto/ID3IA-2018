from __future__ import division
import math as mt
import numpy as np
import copy as cp
import calcEntropy as calc
from node import Node




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
		#print(Atributos[i])
		#print(NovoGanho)
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



def ArvoreDecisao(Dados, Target, Atributos,default):
	Root = Node()


	indice = calc.getIndiceAtributo(Dados,Target)
	maior = "<=50K"
	menor = ">50K"
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
		#return Tree.novo_no(menor)
		return menor
	elif imaior == len(Dados) -1:
		#return Tree.novo_no(maior)
		return maior

	##se acabarem os atributos
	if len(Atributos) == 1:
		return ValorMaisComum(Dados,Target,Atributos)
		#return Tree.novo_no(ValorMaisComum(Dados,Target,Atributos))
	else: 
		a = MelhorAtributo(Dados,Atributos)
		Root.atributo = a
		filhos = {} 
		#print("Atributo: " + a)
		Valores_A = calc.getValoresAtributos(Dados,a)
	#for ind in range(0,len(Atributos)):
	#	if Atributos[ind]==a:
	#		break

		

		for y in range (0,len(Valores_A)):
			Subconjunto=[]
			Subconjunto = calc.makeConjuntoAtributo(Dados,a,Valores_A[y])
			#print("Valor: " +Valores_A[y])
			if len(Subconjunto) == 1:
				#print(ValorMaisComum(Dados,Target,Atributos))
				return Root	
			else:
				filhos[Valores_A[y]] = ArvoreDecisao(Subconjunto,Target,Excluir_vetor(Atributos,a),Root)
				Root.filhos = filhos
	    
	return Root 


def display(Root):
        
		if Root == "<=50K" or Root ==  ">50K":	
			print("\t" + Root)
		else: 
			fil = Root.filhos
			print(Root.atributo)
			for f in fil:
				print(f)
				if f == "<=50K" or f ==  ">50K":
					print("\t" + f)
				else:
					display(Root.filhos[f])  # recursive call


	
