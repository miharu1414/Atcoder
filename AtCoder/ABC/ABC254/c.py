n, k = map(int,input().split())
a = list(map(int,input().split()))

b = sorted(a)

lis = [[] for i in range(k)]
for i in range(n):
    lis[i%k].append(a[i])

for i in range(k):
    lis[i].sort()


new = []
for i in range(n):
    new.append(lis[i%k][i//k])


if new == b:
    print("Yes")
else:
    print("No")