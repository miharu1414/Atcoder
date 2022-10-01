n,q = map(int,input().split())

A = []
for i in range(n):
    a = list(map(int,input().split()))
    A.append(a)
s,t = [],[]
for i in range(q):
    S,T = map(int,input().split())
    print(A[S-1][T])


