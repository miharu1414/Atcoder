h,w = map(int,input().split())
G = [input() for i in range(h)]

i,j = 0,0
visited = [[0] *w for i in range(h)]
while 1:
    if visited[i][j] != 0:
        print(-1)
        exit()
    
    visited[i][j] = 1
    if G[i][j] == 'U' and i != 0:
        i -= 1
    elif G[i][j] == 'D' and i != h-1:
        i += 1
    elif G[i][j] == 'L' and j != 0:
        j -= 1
    elif G[i][j] == 'R' and j != w-1:
        j+= 1
    else:
        break

print(i+1,j+1)