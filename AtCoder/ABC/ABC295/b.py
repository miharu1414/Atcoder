r, c = map(int, input().split())
bombTable = [input() for i in range(r)]
ansTable = [['#']*c for i in range(r)]
for i in range(r):
    for j in range(c):
        if bombTable[i][j] == '.':
            ansTable[i][j] = '.'


def distance(a, b, c, d):
    return abs(a-c) + abs(b-d)


for i in range(r):
    for j in range(c):
        for k in range(r):
            for l in range(c):
                if bombTable[i][j] != '.' and bombTable[i][j] != '#':
                    if int(bombTable[i][j]) >= distance(i, j, k, l):
                        ansTable[k][l] = '.'
ans = ['' for i in range(r)]
for i in range(r):
    for j in range(c):
        ans[i] += ansTable[i][j]
for i in range(r):
    print(ans[i])
