n = int(input())
a = [list(map(int,input().split())) for i in range(n)]
b = [list(map(int,input().split())) for ii in range(n)]
rotate = lambda A: [list(x)[::-1] for x in zip(*A)] 
def Kaiten(a,x):
    ans = [[0 for i in range(len(a))] for i in range(len(a))]
    n = len(a)
    def rotate(a):
        ans = [[0 for i in range(len(a))] for i in range(len(a))]
        for i in range(n):
            for j in range(n):
                ans[i][j] = a[n-j-1][i]
        return ans
    for i in range(x):
        a = rotate(a)
    return  a

flag = False
for i in range(4):
    ans = Kaiten(a,i)
    ok = 1
    for j in range(n):
        for k in range(n):
            if ans[j][k] == 1 and b[j][k] != 1:
                ok = 0
    if ok:
        flag = True
        
if flag:
    print("Yes")
else:
    print("No")