arquivo = open(
    "E:\Workspace\Formação Python Fundamentals/trilha-python-dio/05 - Manipulação de arquivos/teste02.txt", "w"
)


arquivo.write("Testando escrever em arquivos de Texto.")
arquivo.writelines(["\n", "escrevendo", "um", "texto"])
arquivo.close()
