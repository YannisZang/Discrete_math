from itertools import product, combinations, permutations

for t in product({'e', 'u'}, {8, 2, 5}):
    print(*t, sep='')


for s in combinations({8, 2, 5}, 2):
    print(*s, sep=' ')


password = ('b', 'z', 'a', 'd', 'z')
print(type(password))


tuple = ('a', 'c', 'a')
print(tuple)
print(*tuple)
print(*tuple, sep='')


for p in permutations('abc', 2):
    print(p)
