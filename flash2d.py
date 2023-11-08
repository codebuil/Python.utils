import random
from datetime import datetime

def sleeps(i:int):
    
    
    for n in range(i):
        horario_atual = datetime.now()
        segundos = horario_atual.second
        horario_atual = datetime.now()
        segundos2 = horario_atual.second
        while segundos2==segundos:
            horario_atual = datetime.now()
            segundos2 = horario_atual.second

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

def report(xx:int,yy:int,s:str,ss:str,xxx,yyy):
    a1=s
    sss=s
    for n in range(10):
        sss=a1
        a1=setarray(xx,yy,ss,xxx[n],yyy[n],sss)
    print("\x1b[1;1d"+a1)
    

xx=16
yy=11
print("\x1bc\x1b[43;30m")
a1:str=arraysb(xx,yy,"*")
x=[]
y=[]
for n in range(10):
    x.append(random.randint(0,xx-1))
    y.append(random.randint(0,yy-1))

for n in range(200):
    report(xx,yy,a1," ",x,y)
    sleeps(1)
    report(xx,yy,a1,"*",x,y)
    sleeps(1)