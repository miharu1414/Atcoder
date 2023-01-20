n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

ans = [1]*1001

for i in range(n):
    for j in range(1001):
        if a[i]<=j<=b[i]:
            pass
        else:
            ans[j] = 0
print(sum(ans))
            