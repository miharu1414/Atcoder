h,w,x,y = map(int,input().split())
s = [input() for i in range(h)]

ans = [[0]*w for i in range(h)]
for i in range(h):
    for j in range(w):
        mieru = 1
        for k in range(i+1,h):
            if s[k][j] == '#':
                break
            mieru+=1
        for k in range(i-1,-1,-1):
            if s[k][j] == '#':
                break
            mieru+=1
        for k in range(j+1,w):
            if s[i][k] == '#':
                break
            mieru+=1
        for k in range(j-1,-1,-1):
            if s[i][k] == '#':
                break
            mieru+=1
            
        ans[i][j] = mieru

print(ans[x-1][y-1])