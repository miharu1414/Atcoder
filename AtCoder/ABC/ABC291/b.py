n = int(input())
x = list(map(int,input().split()))
ans = sum(x)
x.sort()
for i in range(n):
    ans -= x[i]
    ans -= x[5*n-i-1]
print(ans/3/n)