def mi_generador():
    x = 1
    yield x
    
    x+=1
    yield x
    
    x+=1
    yield x
    
g = mi_generador()

print(next(g))
print(next(g))
print(next(g))