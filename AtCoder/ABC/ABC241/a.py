a = list(map(int,input().split()))
now = a[0]
for i in range(2):
    now = a[now]
print(now)