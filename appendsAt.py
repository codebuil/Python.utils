def appendsat(l:list,news,indexes:int):
    l1=[]
    nn=0
    for n in l:
        if nn == indexes:
            l1=l1+[news]
        l1=l1+[n]
        nn+=1
    return l1

def report(l:list):
    for n in l:
        print(n)




print("\x1bc\x1b[43;30m")
l1=[1,2,3,4,5,6,7,8,9]
print(appendsat(l1,8,3))
