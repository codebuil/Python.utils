
def delitem(l:list,todelete)->list:
  l1=[]
  for n in l:
    if n!=todelete:
      l1.append(n)
  return l1

print("\x1bc\x1b[43;30m")

l1=[1,2,3,4,5]

l2=delitem(l1,3)
print (l2)