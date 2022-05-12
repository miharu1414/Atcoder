n, k = map(int,input().split())
a = list(map(int,input().split()))
s = sum(a[0:k])
b = [[a[i],-i] for i in range(n)]
b.sort()
count = 0
for i in range(k):
    count+=b[n-i-1][0]
if s == count:
    print(-1)
    exit(0)
max = -1
answer = 1<<30
for i in range(n):
    if -b[i][1] >= k:
        if max == -1:
            continue
        answer = min(answer,-b[i][1]-max)
    else:
        if max<-b[i][1]:
            max = -b[i][1]
print(answer)