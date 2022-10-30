n = int(input())
a = list(map(int,input().split()))

pre = [-1]*10**6
depth = [0]*10**6
for i in range(1,n+1):
    pre[2*i] = a[i-1]
    pre[2*i+1] = a[i-1]
    depth[2*i] = depth[a[i-1]] + 1
    depth[2*i+1] = depth[a[i-1]] + 1

for i in range(1,2*n+2):
    print(depth[i])

