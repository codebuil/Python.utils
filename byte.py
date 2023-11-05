
import ctypes

class bbyte:
  def __init__(self,strs:str):
     self.si=0
     self.sizes=len(strs)
     self.buf=ctypes.create_string_buffer(strs.encode()) 
     

  def __next__(self):
   
    if self.sizes>=self.si:
      self.si+=1
      return int.from_bytes(self.buf[self.si-1],byteorder='big') 
    else:
      raise StopIteration


  def __iter__(self):
      return self


print("\x1bc\x1b[43;30m")
for o in bbyte("hello world hi there"):
    print(o)