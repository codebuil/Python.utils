
class allss:
  def __init__(self,l:list):
    self.l=[]
    self.l=(bool(x) for x in l )

  def __bool__(self)->bool:
        for n in self.l:
          if n==False:
            return False
        return True

  
print("\x1bc\x1b[43;30m")

if allss([0,1,2,3,10,12,14,16]):
  print("all")
else:
  print("not all")
