n,m = map(int,input().split())
a = [input() for i in range(2*n)]



syousuu = [[0,-i] for i in range(2*n)]
for i in range(m):
    
    for j in range(n):
        if (a[-syousuu[2*j][1]][i] == 'G' and a[-syousuu[2*j+1][1]][i] == 'C') or \
            (a[-syousuu[2*j][1]][i]=='C' and a[-syousuu[2*j+1][1]][i]=='P') or\
                 (a[-syousuu[2*j][1]][i] == 'P' and a[-syousuu[2*j+1][1]][i] == 'G'):
                     
            syousuu[2*j][0] += 1
            
        if (a[-syousuu[2*j+1][1]][i] == 'G' and a[-syousuu[2*j][1]][i] == 'C') or \
            (a[-syousuu[2*j+1][1]][i]=='C' and a[-syousuu[2*j][1]][i]=='P') or\
                 (a[-syousuu[2*j+1][1]][i] == 'P' and a[-syousuu[2*j][1]][i] == 'G'):
                     
            syousuu[2*j+1][0] += 1
    
    syousuu.sort(reverse=True)
    
ans = [0]*(2*n)
for i in range(2*n):
    print(-syousuu[i][1]+1)
    