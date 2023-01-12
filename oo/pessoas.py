class Pessoas:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade  # ATRIBUTOS DE INSTÂNCIAS
        self.nome = nome
        self.filhos = list(filhos)  # ATRIBUTOS COMPLEXOS

    def cumprimentar(self):  # MÉTODO
        return f'Olá {id(self)}'


if __name__ == '__main__':
    renzo = Pessoas(nome='Renzo')  # OBJETO
    gabriel = Pessoas(nome='gabriel')
    luciano = Pessoas(renzo, gabriel, nome='Luciano')
    print(Pessoas.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'  # Isso é um ATRIBUTO DINAMICO, especifico ao OBJETO
    del luciano.filhos
    print(luciano.__dict__) # Se consegue ver os atributos(ATRIBUTOS DE INSTANCIA) criado para cada OBJETO/
    print(renzo.__dict__)
