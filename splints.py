class splitss:
  def __init__(self,value:str,replaces:str):
    self.value=value
    self.replaces=replaces
    self.i=0
    self.ii=False

  def __next__(self)->str:
    
    while(1):
      if self.ii==True:
        break
      if self.i>=len(self.value):
        break
      a=self.value.find(self.replaces,self.i,len(self.value))
      if a==-1:
        t= self.value[self.i:len(self.value)]
        self.i=len(self.value)
        self.ii=True
        return t
        break
      else:
        t= self.value[self.i:a]
        self.i=a+len(self.replaces)
        return t
  
    raise StopIteration
    
  def __iter__(self):
    return self
    
print("\x1bc\x1b[43;30m")
 
for a in splitss("hello,world,10,10",","):
    print(a)

