from abc import ABC, abstractmethod

#define uma classe abstrata Veículo
class Veiculo(ABC):
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    #define um método abstrato que deve ser implementado em todas as subclasses
    @abstractmethod
    def calcular_velocidade_maxima(self):
        pass

#criamos as subclasses que implementam o método de diferentes maneiras
class Carro(Veiculo):
    def calcular_velocidade_maxima(self):
        #implementação específica para Carro
        return 200

class Moto(Veiculo):
    def calcular_velocidade_maxima(self):
        #implementação específica para Moto
        return 150

#instanciam as classes de carro e moto filhas de veículo (herança: uma vez que herdam 
#do seu contrato a classe abstrata, os metodos e implementações)
carro = Carro("Toyota", "Corolla", 2023)
print("Velocidade máxima do carro:", carro.calcular_velocidade_maxima())

moto = Moto("Honda", "CBR", 2023)
print("Velocidade máxima da moto:", moto.calcular_velocidade_maxima())
