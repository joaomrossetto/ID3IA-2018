from anytree import Node, RenderTree

def ValorMaisComun(Dados, Target, Atributos):

	MaisComum= ""
  
	ganhaMais = getNumeroAparicoes(dados, atributo, '>50K')
	ganhaMenos = getNumeroAparicoes(dados, atributo, '<=50K')

 	if (ganhaMais > ganhaMenos)
 		MaisComum = ">50K"
 	else
 		MaisComum = "<=50K"

 	return MaisComum


def MelhorAtributo (Dados, Target, Atributos):
	
	Melhor = Atributos[0]
	Ganho = 0
	numAtributos = len(Atributos)

    for i in range(0, numAtributos):

    	NovoGanho = calculaGanhoInformacao(Dados, Target)

    	if(NovoGanho > Ganho)
    		Ganho = NovoGanho
    		Melhor = Atributos[i]

	return Melhor;



def ArvoreDecisao(Dados, Target, Atributos):

	indice = getIndiceAtributo(dados,Target)
	maior = ">50K"
	menor = "<=50K"
	imaior = 0
	imenor = 0

	a = ""

	for i range(0,len(dados))
		if imaior > 0 && imenor > 0:
			break
		else if Dados[i][indice] == maior
			imaior ++
		else if Dados[i][indice] == menor
			imenor ++

	#### se tudo for igual 
	if imenor == len(dados):
		return maior
	else if imaior == len(dados)
		return menor

	##se acabarem os atributos
	if len(Atributos) == 0:
		return ValorMaisComum(Dados,Target,Atributos)
	else 
		a = MelhorAtributo(Dados, Target, Atributos)
		Root = Node(a)

	Valores_A = getValoresAtributo(Dados,a)

	for y range (0,len(Valores_A))
		Subconjunto = makeConjuntoATributo(dados,a,Valores_A[y])
		if len(Subconjunto) == 0:
			No = Node(ValorMaisComum(Dados,Target,Atributos), parent=Root)
		else
			ArvoreDecisao (Subconjunto,Target,Atributos.remove(a))

	return No 



	
