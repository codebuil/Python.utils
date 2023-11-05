

class anyss:
  def __init__(self,l:list):
    self.l=[]
    self.l=(bool(x) for x in l )

  def __bool__(self)->bool:
        for n in self.l:
          if n==True:
            return True
        return False

  
print("\x1bc\x1b[43;30m")
if anyss([0,0,0,0,0,1]):
  print("any")
else:
  print("not any")