class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando a bicicleta...")
        print("Bicicleta parada.")

    def correr(self):
        print("Vrummm...")

    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join(f'{chave}={valor}' for chave, valor in self.__dict__.items())}"


b1 = Bicicleta("preto", "caloi", 2025, 1300)
b1.buzinar()
b1.correr()
b1.parar()

print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("preto", "monark", 1999, 300)
b2.buzinar()  # Igual a Bicicleta.buzinar(b2)
print(b2.cor)

print(b2)
