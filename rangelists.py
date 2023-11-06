
class RangesLists:
  def __init__(self,lists):
      self.froms=0
      self.into=len(lists)-1
      self.n=0
      self.lists=[]
      for n in lists:
        
        self.lists.append(n)

  def getlists(self):
      
    return self.lists


  def __iter__(self):
      return self

print("\x1bc\x1b[43;30m")

a=RangesLists(range(1,10,2))

print(a.getlists())
