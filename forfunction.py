
def funcyfunction(ints:int):
    print(ints)


def fornext(froms:int,into:int,stepss:int,funct):
    fors=froms
    while fors<into:
      funct(fors)
      fors+=stepss

print("\x1bc\x1b[43;30m")

s=fornext(1,10,1,funcyfunction)
