
def isertitem(l:list,toinsert,indexes:int)->list:
  l1=[]
  nn=0
  for n in l:
    if nn==indexes:
      l1.append(toinsert)
    l1.append(n)
    nn+=1
  return l1

print("\x1bc\x1b[43;30m")

l1=[1,2,3,4,5]

l2=isertitem(l1,0,3)
print (l2)