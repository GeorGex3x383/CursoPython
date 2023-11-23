def pedir_numero():
    while True:
        try:
            num = int(input("Num: "))
        except:
            print("No es un numero")
        else:
            print(f"Hiciste todo bien {num}")
            break
    print("Gracias")
    
pedir_numero()