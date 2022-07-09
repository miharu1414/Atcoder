n,k ,q = map(int,input().split())
a = list(map(int,input().split()))
l = list(map(int,input().split()))


for i in range(q):
    l[i]-=1

for i in range(q):
    pos = l[i]
    now = a[pos]
    if now == n:
        continue
    boo = 1
    for j in range(k):
        if now+1 == a[j]:
            boo = 0
            break
    if boo:
        a[pos]+=1

print(*a)