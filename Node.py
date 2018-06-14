class No:
    def __init__(self, atributo,aresta):
        self.__atributo = atributo
        self.__aresta=[]
        self.__filhos = []

    @property
    def atributo(self):
        return self.__atributo

    @property
    def aresta(self):
        return self.__aresta

    @property
    def filhos(self):
        return self.__filhos

    def novo_filho(self, No):
        self.__filhos.append(No)