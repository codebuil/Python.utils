def maxs(l:list):
  maxss=l[0]
  i=0
  for i in range(len(l)):
    if l[i]>maxss:
      maxss=l[i]
  return maxss

print("\x1bc\x1b[43;30m")

print(maxs([1,2,3,10,12,34]))
