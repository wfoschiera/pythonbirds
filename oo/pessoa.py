class Pessoa:
    def __init__(self, nome=None, idade=33):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa('Renzo', 35)
    #chamando o método  cumprimentar a partir da classe (Pessoa) e identificando o objeto (p) no método.
    print(Pessoa.cumprimentar(p))
    print(id(p))
    #chamando o método (cumprimentar) a partir do objeto(p)
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)
    p.nome = 'William'
    p.idade = 33
    print(p.nome)
    print(p.idade)
