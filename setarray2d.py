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


def setarray(w:int,h:int,value:str,x:int,y:int,arrayss:str):
  a=arrayss
  a=arrayss[0:y*(w+1)+x]
  a=a+value
  a=a+arrayss[y*(w+1)+x+1:]
  return a

print("\x1bc\x1b[43;30m")
a1:str=arraysb(16,11,"*")
a1=setarray(16,11," ",2,2,a1)
print(a1)
