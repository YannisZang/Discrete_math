def can_extend(perm, i, j, direc, n):
    ul_lr = [[-1, -1], [1, 1]]
    ur_ll = [[-1, 1], [1, -1]]
    sides = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    if n < 0:
        return False
    elif direc == 1:
        for y, x in ur_ll:
            if 0 <= i + y < 5 and 0 <= j + x < 5 and perm[i + y][j + x] == 1:
                return False
        for y, x in sides:
            if 0 <= i + y < 5 and 0 <= j + x < 5 and perm[i + y][j + x] == 2:
                return False
    else:
        for y, x in ul_lr:
            if 0 <= i + y < 5 and 0 <= j + x < 5 and perm[i + y][j + x] == 2:
                return False
        for y, x in sides:
            if 0 <= i + y < 5 and 0 <= j + x < 5 and perm[i + y][j + x] == 1:
                return False

    return True


def extend(perm: list, n: int, rows: int, cols: int, seen: set):
    config_str = ''.join(''.join(str(cell) for cell in row) for row in perm)
    if config_str in seen:
        return False

    if n == 0:
        print("success: ", perm)
        print(len(seen))
        return True

    seen.add(config_str)

    for i in range(rows):
        for j in range(cols):
            if perm[i][j] == 0:
                for direc in range(1, 3):
                    perm[i][j] = direc
                    if can_extend(perm, i, j, direc, n - 1):
                        print(perm)
                        if extend(perm, n - 1, rows, cols, seen):
                            #print("test")
                            return True
                    perm[i][j] = 0
    return False

perm = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

