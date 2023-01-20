class Pessoas:
    olhos = 2  # ATRIBUTO DEFAULT, atributo de classe

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade  # ATRIBUTOS DE INSTÂNCIAS(objeto)
        self.nome = nome
        self.filhos = list(filhos)  # ATRIBUTOS COMPLEXOS

    def cumprimentar(self):  # MÉTODO
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():  # Metodo de CLASSE
        return 42

    @classmethod  # Quando eu quero accessar dados da propria classe
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'
"""A classe pessoa é a classe pai de Homem, e a caracteristica da herança é que a
classe herda da classe pai todos os atributos e metodos."""
class Homem(Pessoas):
    def cumprimentar(self):
        """Eu quero pegar o metodo cumprimentar da classe pai e adicionar algo a esse comportamento"""
        cumprimentar_da_classe = super().cumprimentar()  # Metodo especial que acessa os elementos da classe pai da classe homem.
        #cumprimentar_da_classe = Pessoas.cumprimentar(self) # Utilizar como parametro o objeto
        #cumprimentar_da_classe = self.cumprimentar() Recursao infinita ele retoma o metodo da propria classe
        return f'{cumprimentar_da_classe}. Aperto de mao'  # Sobrescrita de metodo
class Mutante(Pessoas):
    olhos = 3  # Estou sobrescrevendo o atributo da classe pai. Sobreescrita de atributo de dados.

if __name__ == '__main__':
    renzo = Mutante(nome='Renzo')  # OBJETO
    gabriel = Pessoas(nome='gabriel')
    luciano = Homem(renzo, gabriel, nome='Luciano')
    print(Pessoas.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'  # Isso é um ATRIBUTO DINAMICO, especifico ao OBJETO
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos  # Exclui apenas o atributo do objeto e nao da CLASSE.
    print(luciano.__dict__)  # Se consegue ver os atributos(ATRIBUTOS DE INSTANCIA) criado para cada OBJETO/
    print(renzo.__dict__)
    print(luciano.olhos)
    print(luciano.idade)
    print(id(Pessoas.olhos), id(luciano.olhos), id(renzo.olhos))
    print(Pessoas.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoas.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())
    pessoa = Pessoas('Anonimo')
    print(isinstance(pessoa,Pessoas))  # Esse obejto pessoa é do tipo Pessoas ?
    print(isinstance(pessoa,Homem))
    print(isinstance(renzo,Pessoas))  # Esse obejto pessoa é do tipo Pessoas ? Ele é dos dois.
    print(isinstance(renzo,Homem))
    print(renzo.olhos)