#criamos uma classe pai
class Animal:
    def fazer_som(self):
        pass

#criamosas classes filhas que herdam os métodos
class Cachorro(Animal):
    def fazer_som(self):
        return "Au au"

class Gato(Animal):
    def fazer_som(self):
        return "Miau"

#criamos uma função que recebe um animal como parâmetro e "reproduz o som" de qualquer animal passado com parâmetro
def ouvir_som(animal):
    print(animal.fazer_som())

#criamos instâncias das classes filhas
cachorro = Cachorro()
gato = Gato()

#graças ao polimorfismo, podemos obter "sons diferentes" utilizando o mesmo código
ouvir_som(cachorro)
ouvir_som(gato)
