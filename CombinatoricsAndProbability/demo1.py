a = {5, 2, 8, 17, 2}
b = {3, 17, 2, 19, 6, 17}

print(f'Duplicates are removed automatically:')
print(f'a={a}')
print(f'b={b}')
print()

print(f'Size of {a} is {len(a)}')
print(f'Size of {b} is {len(b)}')
print()

print(f'2 belongs to {a}: {2 in a}')
print(f'5 belongs to {a}: {3 in a}')
print(f'2 belongs to {b}: {2 in b}')
print(f'5 belongs to {b}: {5 in b}')
print()

print(f'Union of {a} and {b}: {a.union(b)}')
print(f'Intersection of {a} and {b}: {a.intersection(b)}')
print()

print(f'Set building:')
print(f'Set of odd numbers of {a} is {set(x for x in a if x % 2 == 1)}')
print(f'Set of numbers from {b} that do not belong to {a}:\n'
      f' {set(x for x in b if x not in a)}')