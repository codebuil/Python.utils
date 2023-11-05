def mins(l:list):
  minss=l[0]
  i=0
  for i in range(len(l)):
    if l[i]<minss:
      minss=l[i]
  return minss

print("\x1bc\x1b[43;30m")
print(mins([1,2,3,10,12,34]))
