# TODO: Crie uma função 'elementos_comuns' que receba duas listas de números inteiros separados por espaço:

def elementos_comuns(lista1, lista2):
    set1 = set(map(int, lista1))
    set2 = set(map(int, lista2))

    return list(set1.intersection(set2))


# Leitura das listas
lista1 = input().split()
lista2 = input().split()

# Verifica se todas os elementos das listas podem ser convertidos para inteiros
if all(item.isdigit() for item in lista1) and all(item.isdigit() for item in lista2):
    comuns = elementos_comuns(lista1, lista2)
    print(f"Elementos comuns às duas listas: {comuns}")
else:
    print("Entrada inválida.")
