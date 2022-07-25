h,w = map(int,input().split())
c = [input() for i in range(h)]




dx = [1,0]
dy = [0,1]
visited =[[0]*w for i in range(h)]
ans = 0
cnt = 0
def rec(x,y,cnt):
    visited[x][y]= 1
    global ans
    cnt += 1
    ans = max(ans,cnt)
    for i in range(2):
        if x + dx[i] <h and y + dy[i] <w and c[x+dx[i]][y+dy[i]] == "." and visited[x+dx[i]][y+dy[i]] == 0:
            rec(x+dx[i],y+dy[i],cnt)
    cnt -= 1
        

rec(0,0,0)
if c[0][0] == '#':
    print(0)
else:
    print(ans)