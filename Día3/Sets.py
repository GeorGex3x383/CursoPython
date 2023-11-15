mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

mi_set2 = {1,2,3,4,5}
print(type(mi_set2))
print(mi_set2)

mi_set3 = {1,1,1,1,2,2,3,(1,2,3),4,4,4}
print(type(mi_set3))
print(mi_set3)
print(len(mi_set3))
print(2 in mi_set3)

s1 = {1,2,3}
s2 = {3,4,5,}
s3 = s1.union(s2)
print(s3)
s1.add(4)
print(s1)
s1.remove(3)
print(s1)