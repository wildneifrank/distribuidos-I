class SensorPresenca:
    def __init__(self) -> None:
        pass
    def verificaPresenca(self):
       presenca = input('Tem alguém aí ?#digite 1 ou 0: \n')

       return presenca

while True:
    sensor = SensorPresenca()
    presenca = sensor.verificaPresenca()
    print(presenca)