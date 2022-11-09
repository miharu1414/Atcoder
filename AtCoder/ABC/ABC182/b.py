n = int(input())
a = list(map(int,input().split()))

ans = []
for i in range(2,1001):
    now = 0
    for j in range(n):
        if a[j]%i==0:
            now+=1
    ans.append([now,i])
ans.sort(reverse=True)
print(ans[0][1])