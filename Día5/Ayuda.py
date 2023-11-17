dic = {"clave1":100,"clave2":500}

a = dic.popitem()

print(a,dic)

ejemplo = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
ejemplo2 = ejemplo.lstrip(',:_#%')

print(ejemplo)
print(ejemplo2)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}

marcas_tv = {"Sony", "Philips", "Samsung", "LG"}

conjuntos_aislados=marcas_smartphones.isdisjoint(marcas_tv)

print(conjuntos_aislados)

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"] 
frutas.insert(3,"naranja")
print(frutas)