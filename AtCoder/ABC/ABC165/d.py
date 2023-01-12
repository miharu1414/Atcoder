def f(A,B,x):
    return A*x//B - A*(x//B)
a, b, n = map(int,input().split())

Max = f(a,b,0)
idx = -1
for i in range(max(0,n-2000000),n+1):
    if f(a,b,i)>=Max:
        Max = f(a,b,i)
        idx = i
for i in range(min(a-1,n),n+1,a):
    if f(a,b,i)>=Max:
        Max = f(a,b,i)
        idx = i
print(Max)