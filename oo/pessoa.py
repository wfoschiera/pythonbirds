class Pessoa:
    def __init__(self, *filhos, nome=None, idade=33):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    matheus = Pessoa(nome='Matheus', idade = 1)
    william = Pessoa(nome='William', idade=33)
    antoninho = Pessoa(william, nome='Antoninho', idade=69)
    #chamando o método  cumprimentar a partir da classe (Pessoa) e identificando o objeto (p) no método.
    print(Pessoa.cumprimentar(antoninho))
    print(id(antoninho))
    #chamando o método (cumprimentar) a partir do objeto(p)
    print(antoninho.cumprimentar())
    print(antoninho.nome)
    print(antoninho.idade)
    for filho in antoninho.filhos:
        print(filho.nome)
    #criando atributos em tempo real (na execução)
    antoninho.sobrenome = 'Foschiera'

    william.filhos.append(matheus)

    print(antoninho.__dict__)
    #removendo atributo dinâmico
    del antoninho.sobrenome
    print(antoninho.__dict__)

    for neto in william.filhos:
        print(neto.nome)
    print('acabou')
