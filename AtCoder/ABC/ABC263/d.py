n,l,r = map(int,input().split())
a = list(map(int,input().split()))

f_score = [0] * (n+1)
for i in range(1,n+1):
    f_score[i] = min(f_score[i-1] + a[i-1],i * l)


g_score = [0] * (n+1)
for i in range(1,n+1):
    g_score[i] = min(g_score[i-1] + a[n-i],i * r)

ans = []
for i in range(n+1):
    ans.append(f_score[i]+g_score[n-i])
print(min(ans))