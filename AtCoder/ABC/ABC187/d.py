n = int(input())
ab = [map(int,input().split()) for i in range(n)]
a, b = [list(i) for i in zip(*ab)]

ab = [0]*n
for i in range(n):ab[i] = a[i] + b[i]
Sum_ab = []
for i in range(n):
    Sum_ab.append([ab[i]+a[i],ab[i],a[i]])

Sum_ab.sort(reverse=True)

Aoki = sum(a)
ruiseki_T =[0]*(n+1)
for i in range(n):
    ruiseki_T[i+1] = ruiseki_T[i] + Sum_ab[i][1]
for i in range(n+1):

    if ruiseki_T[i] > Aoki:
        print(i)
        exit()
    Aoki -= Sum_ab[i][2]
    