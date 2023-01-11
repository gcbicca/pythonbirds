class Pessoas:
    def __init__(self, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoas('Luciano')
    print(Pessoas.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())
    print(p.nome)
    p.nome = 'Gabriel'
    print(p.nome)
    print(p.idade)