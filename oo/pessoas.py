class Pessoas:
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoas()
    print(Pessoas.cumprimentar(p))
    print(id(p))
    print(p.cumprimentar())