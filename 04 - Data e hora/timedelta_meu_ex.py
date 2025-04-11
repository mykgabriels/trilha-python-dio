from datetime import datetime, timedelta, date

tipo_carro = "M"  # P, M, G

tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 120
data_atual = datetime.now()

if tipo_carro == "P":
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
    print(f'O carro chegou: {data_atual} e ficará pronto às: {data_estimada}')
elif tipo_carro == "M":
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
    print(f'O carro chegou: {data_atual} e ficará pronto às: {data_estimada}')
else:
    data_estimada = data_atual + timedelta(minutes=tempo_grande)
    print(f'O carro chegou: {data_atual} e ficará pronto às: {data_estimada}')

resultado = datetime.now() - timedelta(hours=1)
print(resultado.time())

print(date.today())
