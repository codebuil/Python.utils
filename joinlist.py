def listjoin(l:list,ll:list)->list:
  l1=[]
  for n in l:
    l1.append(n)
  for n in ll:
    l1.append(n)
  return l1

print("\x1bc\x1b[43;30m")

l1=[1,2,3,4,5]
l11=[6,7,8,9,10,11,12,13,14,15,16,17,18,19]

l2=listjoin(l1,l11)
print (l2)
