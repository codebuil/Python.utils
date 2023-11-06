class openss:
  def __init__(self,froms:str ):
      self.into=open(froms,"r")
      

  def __next__(self):
      try:
        s=self.into.readline()
        
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

for n in openss("my.txt"):
  print(n)