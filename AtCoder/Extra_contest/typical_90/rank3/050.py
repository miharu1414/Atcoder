n, l = map(int,input().split())
mod = 1000000007
dist = [0]*100002
dist[0] = 1
for i in range(n):
    dist[i+1] += dist[i]%mod
    dist[i+1] %=mod
    if i + l<= n:
        dist[i+l] += dist[i]%mod
        dist[i+l] %= mod
print(dist[n])