n = int(input())
a = list(map(int,input().split()))
m = 10**9+7
Sum = a[0]
ans = 0
for i in range(1,n):
    ans = (ans + Sum * a[i])%m
    Sum = (Sum + a[i])%m
print(ans)