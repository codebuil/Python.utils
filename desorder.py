
def desorder(l:list)->list:
  l1=[]
  i=0
  for n in l:
    l11=n
    for m in range(i):
      if l1[m]<l11:
        l13=l1[m]
        l1[m]=l11
        l11=l13
    
    l1.append(l11)
    i+=1
  return l1

print("\x1bc\x1b[43;30m")

l1=["zaa","gz","az","bz","cz"]

l2=desorder(l1)
print (l2)