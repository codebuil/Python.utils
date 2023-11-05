
import random

class rnds:
  def __init__(self,froms:int,into:int ,sizes:int):
      self.froms=froms
      self.into=into
      self.n=froms
      self.sizes=sizes

  def __next__(self):
   
    if self.sizes>0:
      self.sizes-=1
      return random.randint(self.froms, self.into)
    else:
      raise StopIteration


  def __iter__(self):
      return self


print("\x1bc\x1b[43;30m")
for o in rnds(1,50,10):
    print(o)