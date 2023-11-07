
def listcopy(l:list)->list:
  l1=[]
  for n in l:
    l1.append(n)
  return l1

print("\x1bc\x1b[43;30m")

l1=[1,2,3,4,5]

l2=listcopy(l1)
print (l2)