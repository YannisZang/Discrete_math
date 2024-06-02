import itertools as it


count = 0
for c in it.combinations("abcde", 3):
    print("".join(c))
    count += 1

print(count)


n = 1000
count = 0


for i in range(1, n):
    count += i * (i - 1) / 2


print(count)


count2 = 0

for d in it.product(range(10), repeat = 4):
    if 7 in d:
        count2 += 1

print(count2)


count3 = 0


for d in it.product(range(10), repeat = 4):
    if d[0] < d[1] and d[1] < d[2] and d[2] < d[3]:
        count3 += 1


print(count3)
