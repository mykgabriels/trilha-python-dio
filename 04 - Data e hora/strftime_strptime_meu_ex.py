from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "2025-4-11 16:20"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr))

print(datetime.strptime(data_hora_str, mascara_en))
