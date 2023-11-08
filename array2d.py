def Strings(s:str,i:int):
  ss=s
  while i>=len(ss):
    ss=ss+ss
  return ss[0:i]        

def arraysb(x:int,y:int,value:str)->str:
  s=""
  ss=Strings(value,x)+"\n"
  for i in range(y):
      s=s+ss
  return s
  

print("\x1bc\x1b[43;30m")
print(arraysb(16,11,"*"))
