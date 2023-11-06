class listRanges:
  def __init__(self,lists:list):
      self.froms=0
      self.into=len(lists)-1
      self.n=0
      self.lists=lists

  def __next__(self):
      if self.n<=self.into:
          self.n=self.n+1
          return self.lists[self.n-1]
      else:
        raise StopIteration


  def __iter__(self):
      return self


print("\x1bc\x1b[43;30m")

for n in listRanges([9,8,7,6,5,4,3,2,1,0]):
  print(n)
