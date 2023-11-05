def sums(l:list):
  sumss=0
  i=0
  for i in range(len(l)):
    sumss=sumss+l[i]
  return sumss

print("\x1bc\x1b[43;30m")

print(sums([1,2,3,10,12,34]))
