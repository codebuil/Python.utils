class openssbyte:
  def __init__(self,froms:str ):
      self.into=open(froms,"r")
      

  def __next__(self):
      try:
        s=""
        s=self.into.read(1)
        
        if s:
          s=s.replace("\r","")
          return s
        else:
            self.into.close()
            raise StopIteration
      except:
          self.into.close()
          raise StopIteration      


  def __iter__(self):
      return self


print("\x1bc\x1b[43;30m")

for n in openssbyte("my.txt"):
  print(n)