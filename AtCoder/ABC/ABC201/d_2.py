h,w = map(int,input().split())
a = [input() for i in range(h)]


dp = [[0]*w for i in range(h)]
def check(s):
    if s == '+':
        return 1
    else:
        return -1



seen = [[0]*w for i in range(h)]
for i in range(h):
    for j in range(w):
        turn =0 
        if i + j ^ 0:
            turn = 1
        else:
            turn = 0
            
        if i < h-1:
            if turn:
                if dp[i][j] + check(a[i+1][j]) > dp[i+1][j] or not seen[i+1][j]:
                    dp[i+1][j] = dp[i][j] + check(a[i+1][j])
            else:
                if dp[i][j] - check(a[i+1][j]) < dp[i+1][j] or not seen[i+1][j]:
                    dp[i+1][j] = dp[i][j] - check(a[i+1][j])
            
                

            
            
        if j < w-1:
            if turn:
                if dp[i][j] + check(a[i][j+1]) > dp[i][j+1] or not seen[i][j+1]:
                    dp[i][j+1] = dp[i][j] + check(a[i][j+1])
            else:
                if dp[i][j] - check(a[i][j+1]) < dp[i][j+1] or not seen[i][j+1]:
                    dp[i][j+1] = dp[i][j] - check(a[i][j+1])
if dp[h-1][w-1] > 0:
    if h + w ^ 0:
        print("Aoki")
    else:
        print("Takahashi")
if dp[h-1][w-1] == 0:
    print("Draw")

if dp[h-1][w-1] < 0:
    if h + w ^ 0:
        print("Takahashi")
    else:
        print("Aoki")
            
            