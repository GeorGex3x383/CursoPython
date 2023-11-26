from collections import Counter, defaultdict, namedtuple, deque

numeros = [8,6,9,5,4,5,5,5,8,7,4,5,4,4]

print(Counter(numeros))

serie = Counter([1,1,1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,4,4])

print(serie.most_common())

mi_dic = {'uno':'verde','dos':'azul','tres':'rojo'}

print(mi_dic['dos'])

mi_dic2 = defaultdict(lambda:'nada')

mi_dic2['uno'] = 'verde'

print(mi_dic2['dos'])
print(mi_dic2)

Persona = namedtuple('Persona', ['nombre','altura','peso'])

ariel = Persona('Ariel','1.76','79')

print(ariel.altura)
