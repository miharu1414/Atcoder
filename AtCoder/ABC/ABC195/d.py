n,m,q = map(int,input().split())
wv = [map(int,input().split()) for i in range(n)]
w,v = [list(i) for i in zip(*wv)]
x = list(map(int,input().split()))
q = [list(map(int,input().split())) for i in range(q)]


hako = [0]*(m+1)


for k in range(q):
    dp = [[0]*(n+1) for i in range()]
    for i in range(m):
        
        
        for j in range(n)