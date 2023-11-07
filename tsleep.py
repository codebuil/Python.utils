
from datetime import datetime

class tsleeps:
  def __init__(self,froms:int,into:int,sleeps:int ):
      self.froms=froms
      self.into=into
      self.n=froms
      self.sleeps=sleeps

  def __next__(self):
      n=0
      if self.n<=self.into:
        for n in range(self.sleeps):
          horario_atual = datetime.now()
          segundos = horario_atual.second
          horario_atual = datetime.now()
          segundos2 = horario_atual.second
          while segundos2==segundos:
              horario_atual = datetime.now()
              segundos2 = horario_atual.second
        self.n=self.n+1
        return self.n-1
      else:
        raise StopIteration


  def __iter__(self):
      return self


print("\x1bc\x1b[43;30m")

for n in tsleeps(1,10,5):
  print(n)