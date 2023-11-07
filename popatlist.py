
def listpopat(l:list,ats:int)->list:
  l1=[]
  nn=0
  nnn=0
  for n in l:
    if nn !=ats:
        l1.append(n)
    else:
      nnn=n
    nn+=1
  return nnn, l1

print("\x1bc\x1b[43;30m")

l1=[1,2,3,4,5]
nnn=None

nnn,l1=listpopat(l1,3)
print (l1)
print(nnn)