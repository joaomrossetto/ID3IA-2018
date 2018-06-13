import Node

(_ROOT, _DEPTH, _BREADTH) = range(3)


class Arvore:

    def __init__(self):
        self.__nos = {}

    @property
    def nos(self):
        return self.__nos

    def novo_no(self, atributo, mae=None,aresta=None):
        no = Node.No(atributo,aresta)
        self.__nos[atributo] = no
        if mae is not None:
           self.__nos[mae].filhos.append(no)

        return no
    

    def display(self, identifier, depth=_ROOT):
        fil = self.__nos[identifier].filhos
        if depth == _ROOT:
            print("{0}".format(identifier))
        else:
            print("\t"*depth, "{0}".format(identifier))

        depth += 1
        for f in fil:
            self.display(f.atributo, depth)  # recursive call
    