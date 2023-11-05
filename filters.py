
def func1(i):
    if i > 10 :
      return True
    else:
      return False

class filters:
  def __init__(self,func,l:list):
    self.func=func
    self.l=(x for x in l if self.func(x))

  
  def __iter__(self):
    return self.l

print("\x1bc\x1b[43;30m")

for n in filters(func1,[1,2,3,10,12,14,16]):
  print(n)