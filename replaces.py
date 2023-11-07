def replacess(strings:str,value:str,replaces:str):
    s=""
    i=0
    ii=False
    while(1):
      if ii==True:
        break
      if i>=len(strings):
        break
      a=strings.find(value,i,len(strings))
      if a==-1:
        t= strings[i:len(strings)]
        i=len(strings)
        ii=True
        s=s+t
        break
      else:
        t= strings[i:a]+replaces
        i=a+len(value)
        s=s+t

    return s



print("\x1bc\x1b[43;30m")

print(replacess("hello,world,10,10",",","xxxx"))


