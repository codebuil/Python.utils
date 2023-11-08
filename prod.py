def prod(l:list):
    if l:
        prodss=1
        i=0
        for i in range(len(l)):
            prodss=prodss*l[i]
        return prodss
    else:
        return 0
print("\x1bc\x1b[43;30m")

print(prod([2,2,2]))
