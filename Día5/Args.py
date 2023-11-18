def suma(*args):
    total = 0
    for arg in args:
        total+=arg
    return total #Tambien se puede con sum(args)

print(suma(5,6,5))
