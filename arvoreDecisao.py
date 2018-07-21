from __future__ import division
import calcEntropy as calc
from Node import Node
from copy import deepcopy
import pickle
import random

num_nos = []
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

    #global num_nos
    #num_nos = num_nos + 1
    indice = calc.getIndiceAtributo(Dados,Target)
    maior = "<=50K"
    menor = ">50K"
    imaior = 0
    imenor = 0
    a = ""
    for i in range (1,len(Dados)-1):
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
                Root.label = Valores_A[y]
                Root.filhos = filhos

    return Root

def classificador(Dados,Arvore):
    numeroExemplos = len(Dados)
    numAcertos = 0
    acuracia = 0
    indiceClasse = calc.getIndiceAtributo(Dados,'X50k.year')
    for i in range(1,len(Dados)):
        classeExemplo = Dados[i][indiceClasse]
        classeReal = avaliaExemplo(Arvore, Dados[i], Dados)
        if classeExemplo == classeReal:
            numAcertos += 1
        acuracia = numAcertos/(numeroExemplos-1)
    #print("A acuracia foi de :",acuracia)
    return acuracia


def avaliaExemplo(NoRaiz, Exemplo, Dados):
    nosVisitados = 0
    while len(NoRaiz.filhos) != 0:
        atributoNo = NoRaiz.atributo
        indiceAtributo = calc.getIndiceAtributo(Dados, atributoNo)
        valorAtributoExemplo = Exemplo[indiceAtributo]
        valorAtributoAux =""
        for a in NoRaiz.filhos:
           if valorAtributoAux == "":
              valorAtributoAux = a
           elif valorAtributoExemplo == a:
                valorAtributoAux = a
        NoRaiz = NoRaiz.filhos[valorAtributoAux]
        nosVisitados += 1
        if NoRaiz == '<=50K' or NoRaiz == '>50K':
            return NoRaiz
    return NoRaiz


def getRegras(No):
    regras = []
    regraAteEntao = []
    getRegrasRec(No, regraAteEntao, regras, 0)


def getRegrasRec(No, RegraAteEntao, regras, Indice):
    if not No:
        return []
    else:
        while len(No.filhos) != 0:
            aux = [No.atributo, No.filhos[Indice]]
            RegraAteEntao.append(aux)
            if No == '<=50K' or No == '>50K':
                RegraAteEntao.append(No)
                regras.append(RegraAteEntao)
                indice += 1
                return
            getRegrasRec(No.filhos[Indice], RegraAteEntao, regras, Indice)

def compara_acuracia (Root, Dados):
    acuraciaAntiga = classificador(Dados,Root)
    novoNo = deepcopy(Root)
    if len(novoNo.filhos) != 0:
        novoNo.filhos = {}
        acuraciaNova = classificador(Dados,novoNo)
        if acuraciaNova > acuraciaAntiga:
            Root.filhos = {}
            return Root
    return Root

def comp_acc (Root, no, Dados, ocorrencia):
    global num_nos
    acuraciaAntiga = classificador(Dados,Root)
    num_nos.append(acuraciaAntiga)
    #no_file = open(r'no_file.pkl','wb')
    #pickle.dump(no,no_file)
    #no_file.close()
    filhos = no.filhos[no.label]
    #no.label = ocorrencia
    no.filhos[no.label] = ocorrencia
    #no=ocorrencia
    acuraciaNova = classificador(Dados,Root)
    if acuraciaNova > acuraciaAntiga:
        print(acuraciaNova)
        return Root
    elif acuraciaNova == acuraciaAntiga:
        return Root
    else:
        #recover_file = open(r'no_file.pkl','rb')
        #no_recover = pickle.load(recover_file)
        #recover_file.close()
        #Root = no_recover
        ##no.filhos = no_recover.filhos
        no.filhos[no.label] = filhos
        return Root

def poda2(Root, no, Dados, sinaliza_root):
    menor = "<=50K"
    maior = ">50K"
    ocorrencia = ''
    if len(no.filhos) != 0:
        #cont_folha = 0
        cont_menor = 0
        cont_maior = 0
        add_menor = 0
        add_maior = 0
        for i in no.filhos:
            if no.filhos[i] == menor:
                cont_menor +=1
            elif no.filhos[i] == maior:
                cont_maior +=1
            else:
                add_menor, add_maior = poda2(Root,no.filhos[i],Dados,1)

        cont_menor += add_menor
        cont_maior += add_maior
        #cont_folha = cont_menor + cont_maior
        #if ocorrencia=='':
        if cont_menor > cont_maior:
            #no.recorrente = menor
            Root = comp_acc(Root, no, Dados, menor) #Representa maioria "<=50K"
        elif cont_maior > cont_menor:
            #no.recorrente = maior
            Root = comp_acc(Root,no,Dados,maior) #Representa maioria ">50K" talvez enviese o modelo
        else:
            randomiza = random.choice([menor, maior])
            #no.recorrente = randomiza
            Root = comp_acc(Root,no,Dados,randomiza)

        if sinaliza_root == 1:
            return cont_menor, cont_maior
    global num_nos
    return Root, num_nos

def poda (Root, Dados):
    temp = []
    temp.append(Root)
    while len(temp) != 0:
        n = temp.pop(0)
        n = compara_acuracia(n, Dados)
        filhos = n.filhos
        if len(filhos) != 0:
            for i in filhos:
                if filhos[i] != '<=50K' and filhos[i] != '>50K':
                     temp.append(filhos[i])
    return Root




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


def ehNoPaiFolha(Root):
    if Root.filhos[next(iter(Root.filhos))] =='<=50K' or Root.filhos[next(iter(Root.filhos))] ==">50K" :
        return True


def getCaminhoMaisUsado(Dados,Arvore):
    indiceClasse = calc.getIndiceAtributo(Dados,'X50k.year')
    for i in range(1,len(Dados)):
        avaliaExemploMaisUsado(Arvore, Dados[i], Dados)


def avaliaExemploMaisUsado(NoRaiz, Exemplo, Dados):
    while len(NoRaiz.filhos) != 0:
        atributoNo = NoRaiz.atributo
        indiceAtributo = calc.getIndiceAtributo(Dados, atributoNo)
        valorAtributoExemplo = Exemplo[indiceAtributo]
        valorAtributoAux =""
        for a in NoRaiz.filhos:
           if valorAtributoAux == "":
              valorAtributoAux = a
           elif valorAtributoExemplo == a:
                valorAtributoAux = a
        if NoRaiz != '<=50K' or NoRaiz != '>50K':
            if ehNoPaiFolha(NoRaiz):
                NoRaiz.numAcessos = NoRaiz.numAcessos + 1
                print('o numero de acessos a esse nó pai de folha é ' + str(NoRaiz.numAcessos))
        NoRaiz = NoRaiz.filhos[valorAtributoAux]
        if NoRaiz == '<=50K' or NoRaiz == '>50K':
            return NoRaiz
    return NoRaiz


def visitaPrintandoRegras(Raiz):
    lista = []
    visita(Raiz)

def visita(Raiz, Caminho):
    Caminho.add(Raiz.atributo)
    if Raiz == '<=50K' or Raiz == '>50K':
        print(Caminho)
    for i in Raiz.filhos:









