arquivo = open(
    "E:\Workspace\Formação Python Fundamentals/trilha-python-dio/05 - Manipulação de arquivos\lorem.txt", "r"

)

print(arquivo.read())
print(arquivo.readline())
print(arquivo.readlines())

# while len(linhas := arquivo.readline()):
#    print(linhas)
arquivo.close()
