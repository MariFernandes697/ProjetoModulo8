from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self,nome, idade):
        self._nome = nome
        self.__idade = idade

    
    def setNome(self,nome):
        self._nome = nome
    
    def setIdade(self,idade):
        self.__idade = idade

    def getNome(self):
        return self._nome
    
    def getIdade(self):
        return self.__idade
    

    @abstractmethod
    def mostrar(self):
        pass
