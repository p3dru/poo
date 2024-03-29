#veiculo é a classe pai que tem os atributos marca e modelo e o método mover
class Veiculo:
  #__init__(self, atributo, atributo) representa o construtor 
  def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo

  def mover(self):
    print(f"O veículo {self.marca} {self.modelo} está se movendo.")

#carro é a classe filha que herda atributos de seu pai
class Carro(Veiculo):
  def __init__(self, marca, modelo, tipo):
    #super é a palavra reservada em python que inicializa atributos de uma classe pai na classe filha
    #como marca e modelo, são definidos pelo seu pai, não é necessário reescrever o código inicializando-o
    super().__init__(marca, modelo)
    #como tipo é um atributo próprio, ele precisa ser inicializado com "self" 
    self.tipo = tipo

  #método próprio da classe filha
  def dirigir(self):
    print(f"O carro {self.marca} {self.modelo} está dirigindo.")

carro = Carro("Fiat", "Mobi", "hatch")

#carro pode acessar o método mover() pois herda de seu pai
carro.mover()
#dirigir é da própria classe filha
carro.dirigir()