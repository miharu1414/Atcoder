n = int(input())
a  = list(map(int,input().split()))
q = int(input())
bc = [map(int,input().split()) for i in range(q)]
b,c = [list(i) for i in zip(*bc)]

Num = [0 for i in range(10**5+1)]

Ans = 0

for i in range(n):
    Num[a[i]]+=1
    Ans += a[i]

for i in range(q):
    X = Num[b[i]]
    Num[b[i]] = 0
    Num[c[i]] += X
    Ans += c[i]*X
    Ans -= b[i]*X
    print(Ans)

