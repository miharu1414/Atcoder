
n = int(input())
a = [[]for i in range(n+1)]
a[1].append(1)
for i in range(2,n+1):
    for j in range(i):
        if j == 0 or j == i-1:
            a[i].append(a[i-1][0])
        else:
             a[i].append(a[i-1][j-1]+a[i-1][j])
for i in range(1,n+1):
    print(*a[i])