h,w = map(int,input().split())
a = [input() for i in range(h)]

inf = 1<<30
dp = [[[0,0] for j in range(w)] for i in range(h)]
def check(s):
    if s == '+':
        return 1
    else:
        return -1
seen = [[0]*w for i in range(h)]
dp[0][0][0] = 0
seen[0][0] = 1
for i in range(h):
    for j in range(w):
        turn =0 
        if i + j ^ 0:
            turn = 1
        else:
            turn = 0
            
        if i < h-1:
            if dp[i][j][turn] + check(a[i+1][j]) > dp[i+1][j][turn] or not seen[i+1][j]:
                dp[i+1][j][turn] = dp[i][j][turn] + check(a[i+1][j])
                dp[i+1][j][~turn] = dp[i][j][~turn] 
        
            
        if j < w-1:
            if dp[i][j][turn] + check(a[i][j+1]) > dp[i][j+1][turn]or not seen[i][j+1]:
                dp[i][j+1][turn] = dp[i][j][turn] + check(a[i][j+1])
                dp[i][j+1][~turn] = dp[i][j][~turn] 
if dp[h-1][w-1][0] > dp[h-1][w-1][1]:
    if h + w & 1:
        print("Aoki")


    else:
        print("Takahashi")



if dp[h-1][w-1][0] == dp[h-1][w-1][1]:
    print("Draw")
if dp[h-1][w-1][0] < dp[h-1][w-1][1]:
    if h + w & 1:
        print("Takahashi")
    else:
        print("Aoki")

            
            