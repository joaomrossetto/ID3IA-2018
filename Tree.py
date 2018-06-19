import Node

(_ROOT, _DEPTH, _BREADTH) = range(3)


class Arvore:

    def __init__(self):
        self.__nos = {}

    @property
    def nos(self):
        return self.__nos

    def novo_no(self, atributo, mae=None,aresta=None):
        

        if atributo == '<=50K' or atributo== '>50K':
           no = Node.No(atributo + "|" + aresta + "|" + mae, aresta)
           self.__nos[atributo + "|" + aresta + "|" + mae] = no
        else:
           no = Node.No(atributo, aresta)
           self.__nos[atributo] = no 
        
        if mae is not None:
           self.__nos[mae].filhos.append(no)

        return no
    

    def display(self, identifier, depth=_ROOT):
        
        fil = self.__nos[identifier].filhos
        arestas = self.__nos[identifier].aresta
        if depth == _ROOT:
            print("{0}".format(identifier))
        else:
            print("\t"*depth, "{0}".format(identifier))

        depth += 1
        i=0
        for f in fil:
            print("Aresta: " + arestas[i])
            i = i+1
            if f == "<=50K" or f ==  ">50K":
                print("\t" + f)
            else:
                self.display(f.atributo, depth)  # recursive call
    