def adds(i):
    
      return i+i
class maps:
  def __init__(self,func,l:list):
    self.func=func
    self.l=(self.func(x) for x in l )

  
  def __iter__(self):
    return self.l

print("\x1bc\x1b[43;30m")
for n in maps(adds,[1,2,3,10,12,14,16]):
  print(n)
