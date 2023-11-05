
class countss:
  def __init__(self,l:list,value):
    self.l=[]
    self.l=(x for x in l if x==value)
    self.n=0
    for n in self.l:
      self.n+=1
    
  
  def __len__(self):
    return self.n
    
print("\x1bc\x1b[43;30m") 
a=countss([1,1,1,3,3,4,5,5],1)
print(len(a))
