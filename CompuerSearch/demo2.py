
def can_be_extended_to_solution(perm):
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True

def extend(perm, n):
    if len(perm) == n:
        print(perm)
        exit()

    for k in range(n):
        if k not in perm:
            perm.append(k)

            # if existing perm has a solution, extend
            if can_be_extended_to_solution(perm):
                extend(perm, n)
            # if existing perm has no solution remove last element and append continue loop
            perm.pop()


def queens(n: int, i: int, a: list, b: list, c: list):
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a

count = 0

for solution in queens(8, 0, [], [], []):
    print(solution)
    count = count + 1

print(count)