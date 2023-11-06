def finelist(l:list,separator:str)->str:
  lll=len(l)
  llll=0
  s=""
  for ll in l:
      llll+=1
      s=s+str(ll)
      if lll>llll:
          s=s+separator
  return s

print("\x1bc\x1b[43;30m")

s=finelist([1,2,3,4,5,6,7,8,9,0],"\n")
print(s)

