class Pessoa:
    #atributo público
    nome = 'Nome Público'

    #Em python '_atributo / _metodo' representam atributos e métodos protegidos
    #'__atributo / __metodo' representam atributos e métodos privados
     
    #atributo protegido (acessível dentro da classe e suas subclasses)
    _idade = 30

    #atributo privado (acessível apenas dentro da classe)
    __idade_privada = 40

    #__init__(self, atributo, atributo) representa o construtor 
    def __init__(self, nome, idade):
        #atributo público
        self.nome = nome
        #atributo protegido
        self._idade = idade
        #atributo privado
        self.__set_idade_privada(idade)

    #método para acessar o atributo privado
    def get_idade_privada(self):
        return self.__idade_privada

    #método para definir o atributo privado
    def __set_idade_privada(self, idade):
        self.__idade_privada = idade

    #método protegido (acessível dentro da classe e suas subclasses)
    def _metodo_protegido(self):
        return f"Idade: {self._idade}"

    #método público
    def metodo_publico(self):
        return f"Nome: {self.nome}"

#criando a instância
pessoa = Pessoa('Pedro', 39)

#acessando a classe pessoa de dentro da classe
#atributo público
print(pessoa.nome)

#acessando o atributo protegido (acessível dentro da classe e suas subclasses)
print(pessoa._idade)

#acessando de fora da classe
#para isso, é necessário criamos métodos para acessarmos esses atributos (encapsulamento)

#acessando o atributo privado 
print(pessoa.get_idade_privada())

#chamando um método protegido
print(pessoa._metodo_protegido())

#chamando um método público
print(pessoa.metodo_publico()) 