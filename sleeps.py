
from datetime import datetime

def seeps(i:int):
    
    
    for n in range(i):
        horario_atual = datetime.now()
        segundos = horario_atual.second
        horario_atual = datetime.now()
        segundos2 = horario_atual.second
        while segundos2==segundos:
            horario_atual = datetime.now()
            segundos2 = horario_atual.second



print("\x1bc\x1b[43;30m")
seeps(10)