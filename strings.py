def Strings(s:str,i:int):
    ss=s
    while i>=len(ss):
      ss=ss+ss
    return ss[0:i]        


print("\x1bc\x1b[43;30m")
print(Strings("*",100))
