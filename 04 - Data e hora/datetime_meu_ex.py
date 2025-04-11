from datetime import date, datetime, time

data_hj = date(2025, 4, 11)

print(data_hj)
print(date.today())

data_hora = datetime(2025, 4, 11, 10, 25, 55)
print(data_hora)
print(datetime.today())

hora = time(10, 28, 0)
print(hora)


def hora_atual():
    print(datetime.today())


hora_atual()
