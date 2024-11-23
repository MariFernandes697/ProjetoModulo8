from atividade6 import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, porte):
        super().__init__(nome, idade)
        self.__porte = porte
    
    def setPorte(self, porte):
        self.__porte = porte

    def getPorte(self):
        return self.__porte

    def mostrar(self):
        return (f" O cachorro é o: {self.getNome()}, ele tem {self.getIdade()} anos e seu porte é {self.getPorte()}")
    
#c = Cachorro ("Duck", "10", "grande", "Border Collie")
#print(c.mostrar())