conv = ["a", "b", "c", "d", "e", "f", "g", "h"]
N = [[[] for _ in range(8)] for _ in range(8)]
car_N = [[0 for _ in range(8)] for _ in range(8)]
P = [[0 for _ in range(64)] for _ in range(64)]

def to_chess(r, c):
    return f"{conv[r]}{c+1}"

for r in range(8):
    a = 0
    for c in range(8):
        if r - 2 > -1:
            if c - 1 > -1:
                N[r][c].append((r - 2,c - 1))
                car_N[r][c] += 1
            if c + 1 < 8:
                N[r][c].append((r - 2,c + 1))
                car_N[r][c] += 1

        if r + 2 < 8:
            if c - 1 > -1:
                N[r][c].append((r + 2,c - 1))
                car_N[r][c] += 1
            if c + 1 < 8:
                N[r][c].append((r + 2,c + 1))
                car_N[r][c] += 1

        if c - 2 > -1:
            if r - 1 > -1:
                N[r][c].append((r - 1,c - 2))
                car_N[r][c] += 1
            if r + 1 < 8:
                N[r][c].append((r + 1,c - 2))
                car_N[r][c] += 1

        if c + 2 < 8:
            if r - 1 > -1:
                N[r][c].append((r - 1,c + 2))
                car_N[r][c] += 1
            if r + 1 < 8:
                N[r][c].append((r + 1,c + 2))
                car_N[r][c] += 1

for r in range(8):
    for c in range(8):
        x = r * 8 + c
        for (nr, nc) in N[r][c]:
            y = nr * 8 + nc
            P[x][y] = 1 / car_N[r][c]

print(f"x\tN(x)\t|N(x)|")
for i in range(8):
    for j in range(8):
        print(f"{conv[i]}{j + 1}\t{car_N[i][j]}", end="\t")
        for k in range(len(N[i][j])):
            print(to_chess(*N[i][j][k]), end="  ")
        print()

print(P)