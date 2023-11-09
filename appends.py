def appends(l:list,news):
    l1=[]
    for n in l:
        l1=l1+[n]
    l1=l1+[news]
    return l1

def report(l:list):
    for n in l:
        print(n)




print("\x1bc\x1b[43;30m")
l1=[1,2,3,4,5,6,7,8,9]
print(appends(l1,8))
