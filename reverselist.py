
def reverseslist(l:list)->list:
  lll=len(l)
  llll=lll
  s=[]
  for ll in range(lll):
      llll-=1
      s.append(l[llll])
      
  return s

print("\x1bc\x1b[43;30m")

s=reverseslist([1,2,3,4,5,6,7,8,9,0])
print(s)
