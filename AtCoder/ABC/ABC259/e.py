n = int(input())
m = []
p = []
e = []

for i in range(n):
    M = int(input())
    m.append(M)
    pi =[]
    ei = []
    for j in range(M):
        P,E = map(int,input().split())
        pi.append(P)
        ei.append(E)
    p.append(pi)
    e.append(ei)

div = dict()
for i in range(n):
    for j in range(m[i]):
        if p[i][j] not in div:
            div[p[i][j]] = e[i][j]
        else:
            div[p[i][j]] = max(e[i][j],div[p[i][j]])
max = dict()
for i in range(n):
    for j in range(m[i]):
        if e[i][j] == div[p[i][j]]:
            if p[i][j] not in max:
                max[p[i][j]] = 1
            else:
                max[p[i][j]] += 1


ans = 1
if n == 1:
    print(ans)
    exit()
elif n == 2:
    if m[0] != m[1]:
        print(2)
        exit()
    else:
        flag = 1
        for i in range(m[0]):
            if p[0][i]!=p[1][i]:
                flag = 0
            elif e[0][i]!=e[1][i]:
                flag = 0
        if flag:
            print(1)
        else:
            print(2)
        exit()

for i in range(n):
    num = 0
    for j in range(m[i]):
        if div[p[i][j]] == e[i][j] and max[p[i][j]] == 1:
            num+=1
    if num:
        ans += 1
if ans > n:
    ans -= 1

print(ans)