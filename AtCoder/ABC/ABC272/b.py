n,m=map(int,input().split())
x = []
k = []
sanka = [[0]*(m) for i in range(n+1)]
for i in range(m):
    a = list(map(int,input().split()))

    for j in range(1,a[0]+1):
        sanka[a[j]][i] = 1

flag = 1
for i in range(1,n+1):

    for j in range(i+1,n+1):
        flag2 = 0
        for k in range(m):
            if sanka[i][k] == 1 and sanka[j][k] == 1:
                flag2 = 1
        if flag2 == 0:
            flag = 0
if flag:
    print("Yes")
else:
    print("No")
