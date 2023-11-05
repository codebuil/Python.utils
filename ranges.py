
class tranges:
  def __init__(self,froms:int,into:int ):
      self.froms=froms
      self.into=into
      self.n=froms

  def __next__(self):
      if self.n<=self.into:
          self.n=self.n+1
          return self.n-1
      else:
        raise StopIteration


  def __iter__(self):
      return self


print("\x1bc\x1b[43;30m")

for n in tranges(1,10):
  print(n)