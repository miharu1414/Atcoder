n = int(input())
a = list(map(int,input().split()))

mod = [0]*(1000001)
a.sort()

for i in range(n):
    now = a[i]
    if mod[a[i]] > 0:
        mod[a[i]] +=  1
        continue
    while now <= 1000000:
        mod[now] += 1
        now += a[i]

ans = 0
for i in range(n):
    if mod[a[i]] == 1:
        ans += 1
print(ans)