def listpop(l:list)->list:
  l1=[]
  nn=0
  nnn=0
  for n in l:
    if nn !=len(l)-1:
        l1.append(n)
    else:
      nnn=n
    nn+=1
  return nnn, l1

print("\x1bc\x1b[43;30m")

l1=[1,2,3,4,5]
nnn=None

nnn,l1=listpop(l1)
print (l1)
print(nnn)
