class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # TODO: Crie um método para retornar as informações formatas com Nome e Idade:
    def format(self, nome, idade):
        self.nome = nome
        self.idade = idade
        return print(f"Nome: {self.nome}, Idade: {self.idade}")


# Entrada do usuário
nome = input()
idade = int(input())

# TODO: Crie uma instância da pessoa:
pessoa = Pessoa(nome, idade)

# TODO: Chame o método para retornar as informações formatadas e imprima o resultado:
pessoa.format(nome, idade)
