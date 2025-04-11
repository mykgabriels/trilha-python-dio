import pytz
from datetime import datetime

data_atual = datetime.now(pytz.timezone("Europe/Oslo"))
data_atual2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data_atual)
print(data_atual2)
