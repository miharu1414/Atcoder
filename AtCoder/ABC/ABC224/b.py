h,w  = map(int,input().split())
a = [list(map(int,input().split())) for  i in range(h)]
flag= 1
for  i in range(h):
    for i2 in range(i,h):
        for j in range(w):
            for j2 in range(j,w):
                if a[i][j] + a[i2][j2] > a[i2][j] + a[i][j2]:
                    flag = 0
if flag:
    print("Yes")
else:
    print("No")