n,k = map(int,input().split())
p = list(map(int,input().split()))

atai = p[0]
for i in range(k):
    atai = min(p[i],atai)
for i in range(k,n+1):
    if atai 
