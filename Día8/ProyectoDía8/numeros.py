def ticket_perfumeria():
    for n in range(1,10000):    
        yield f"P-{n}"
        
def ticket_Farmacia():
    for n in range(1,10000):    
        yield f"F-{n}"
        
def ticket_cosmeticos():
    for n in range(1,10000):    
        yield f"C-{n}"

p = ticket_perfumeria()
f = ticket_Farmacia()
c = ticket_cosmeticos()

def decorar_ticket(rubro):
    
    print("Su turno es:")
    if rubro == 'p':
        print(next(p))
    elif rubro == 'f':
        print(next(f))
    else:
        print(next(c))
    print("Aguarde y será atendido.\n")