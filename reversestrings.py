def reversesstrings(l:str)->str:
  lll=len(l)
  llll=lll
  s=""
  for ll in range(lll):
      llll-=1
      s=s+l[llll]
      
  return s

print("\x1bc\x1b[43;30m")

s=reversesstrings("[1,2,3,4,5,6,7,8,9,0]")
print(s)

