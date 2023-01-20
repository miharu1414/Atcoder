n = int(input())
a = list(map(int,input().split()))

pre  = [0 for i in range(n+1)]
for i in range(n-1):
    pre[a[i]-1] +=1
for i in range(n):
    print(pre[i])