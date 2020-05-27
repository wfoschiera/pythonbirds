class Pessoa:
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    p = Pessoa()

    #chamando o método  cumprimentar a partir da classe (Pessoa) e identificando o objeto (p) no método.
    print(Pessoa.cumprimentar(p))

    print(id(p))

    #chamando o método (cumprimentar) a partir do objeto(p)
    print(p.cumprimentar())