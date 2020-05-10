'''O valor será o mesmo para todos os objetos ?
  Se sim, criar no Atributos de Classe.
  Se não, deve criar no Atributo de instância'''

class Pessoa:
    olhos = 2   #  Atributo default   ou   Atributo de Classe

    def __init__(self, *filhos, nome=None, idade=35):     # Atributos de instância
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod   # cria um metodo independente do objeto a ser executado    (@ - decorator)
    def metodo_estatico():
        return 42

    @classmethod      # Acessa dados da propria classe
    def nome_e_atributo_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    luciano.sobrenome = 'Ramalho'  # Atributos dinâmicos
    print(luciano.sobrenome)      # luciano é o objeto  e  sobrenome é o seu atributo
    print(luciano.__dict__)
    del luciano.filhos        # Atributos de instância fica presente na  __dict__
    luciano.olhos = 1        # Atributos dinâmicos
    print(luciano.__dict__)
    print(renzo.__dict__)
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos) )
    del luciano.olhos        # Atributos de instância fica presente na  __dict__
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos) )
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributo_de_classe(), luciano.nome_e_atributo_de_classe())
