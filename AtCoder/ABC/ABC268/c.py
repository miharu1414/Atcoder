n = int(input())
p = list(map(int,input().split()))

dist = [0]*n
for i in range(n):

    dist[p[i]] = (p[i] - i)%n


cnt = [0]*n
for i in range(n):
    cnt[dist[i]] +=1



ans1 = 0
for i in range(n):
    if i == 0:
        ans = cnt[n-1] + cnt[i] + cnt[i+1]
    elif i == n-1:
        ans = cnt[n-2] + cnt[i] + cnt[0]
    else:
        ans = cnt[i-1] + cnt[i] + cnt[i+1]
    ans1 = max(ans1,ans)
print(ans1)