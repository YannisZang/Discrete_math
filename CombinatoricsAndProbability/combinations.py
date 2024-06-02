import itertools as it

# Tuples are ordered selections with repetitions. The number of tuples is n^k

for t in it.product('abc', repeat=2):
    print(*t, sep='', end=' ')
print('\n')

# Permutations are ordered selections without repetitions. The number of permutations is n! / (n-k)!

for t in it.permutations('abc', 2):
    print(*t, sep='', end=' ')
print('\n')


# Combinations are unordered selections without repetitions. Also known as sets. n | k
# The number of combinations is n! / ( (n-k)! * k!)

for t in it.combinations('abc', 2):
    print(*t, sep='', end=' ')
print('\n')

# Combinations with repetitions are unordered selections with repetitions. Also known as multisets. k + n - 1 | n - 1

for t in it.combinations_with_replacement('abc', 2):
    print(*t, sep='', end=' ')
print('\n')

for t in it.combinations_with_replacement('abc', 4):
    print(*t, sep='', end=' ')
print('\n')

count = 0
for t in it.product(range(10), repeat = 4):
    if t[0] >= t[1] and t[1] >= t[2] and t[2] >= t[3]:
        count += 1

print(count)

count3 = 0
for t in it.combinations(range(44), 6):
    count3 += 1

print('\n')
print(count3)

