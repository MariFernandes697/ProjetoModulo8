from atividade6 import Animal

class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.__raca = raca

    def setRaca(self, raca):
        self.__raca = raca

    def getRaca(self):
        return self.__raca
    
    def mostrar(self):
        return (f" O gato é o: {self.getNome()}, ele tem {self.getIdade()} anos e sua raça é {self.getRaca()}")
    
#c = Gato ("Francisco", "2", "Persa")
#print(c.mostrar())