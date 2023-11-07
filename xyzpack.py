class xyzc:
  def __init__(self,value:str):
    self.value=value
    self.replaces=';'
    self.i=0
    self.ii=False

  def __next__(self)->list:

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
        return t.split (",")
        break
      else:
        t= self.value[self.i:a]
        self.i=a+len(self.replaces)
        return t.split (",")

    raise StopIteration

  def __iter__(self):
    return self

print("\x1bc\x1b[43;30m")

for x,y,z,c in xyzc("0,0,0,6;0,0,1,6;0,1,0,6;1,0,0,6"):
    print(f"X:{x},Y:{y},Z:{z},Color:{c}")

