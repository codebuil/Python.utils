def avaregess(l:list)->int:
  avaregessss=0
  i=0
  countss=0
  if l:
    
  
    for i in range(len(l)):
      avaregessss=avaregessss+l[i]
      countss+=1
    return int(avaregessss/countss)
  else:
    return 0


print("\x1bc\x1b[43;30m")

print(avaregess([1,2,3,10,12,34]))
