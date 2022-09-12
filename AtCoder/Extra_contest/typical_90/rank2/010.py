n = int(input())
xy = [map(int, input().split()) for _ in range(n)]
c,p = [list(i) for i in zip(*xy)]
point =[0]*n

q = int(input())
xy = [map(int, input().split()) for _ in range(q)]
l,r = [list(i) for i in zip(*xy)]

ruiseki_1 = [0]*(n+1)
ruiseki_2 = [0]*(n+1)

for i in range(n):

    if c[i] == 1:
        ruiseki_1[i+1]+= ruiseki_1[i] + p[i]
        ruiseki_2[i+1] = ruiseki_2[i]
    else:
        ruiseki_2[i+1] += ruiseki_2[i] +p[i]
        ruiseki_1[i+1] += ruiseki_1[i]
    
for i in range(q):
    ans = []
    ans.append(ruiseki_1[r[i]]-ruiseki_1[l[i]-1])
    ans.append(ruiseki_2[r[i]]-ruiseki_2[l[i]-1])
    print(*ans)