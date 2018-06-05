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
	#Se Attributes for vazio, retorne o nó Root, com rótulo = valor mais comum de Target_Attribute em Examples
	if len(Atributos) - 1 <= 0 
	
	Default = ValorMaisComum(Dados, Target, Atributos)

	.
	.
	.
