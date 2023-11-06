def fancylist(l:list):
  lll=len(l)
  llll=0
  for ll in l:
      llll+=1
      print (str(ll),end="")
      if lll>llll:
          print (" , ",end="")
      else:
        print("")

print("\x1bc\x1b[43;30m")

fancylist([1,2,3,4,5,6,7,8,9,0])


