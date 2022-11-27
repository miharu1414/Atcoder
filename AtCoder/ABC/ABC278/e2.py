
H,W,n,h,w = map(int,input().split())
b = [list(map(int,input().split())) for i in range(H)]

num = [0]*301
for i in range(H):
    for k in range(W):
        num[b[i][k]] += 1



ANS = []


for i in range(H-h+1):


    for yoko in range(w):
        for tate in range(h):
            num[b[i+tate][yoko]] -= 1
    cnt = 0
    for k in range(1,n+1):
        if num[k] == 0:
            cnt += 1
            
    ans = []
    ans.append(n-cnt)
    
    for yoko in range(w,W):
        
        for tate in range(h):
            num[b[i+tate][yoko]] -= 1



            num[b[i+tate][yoko-w]] += 1
        cnt = 0
        for k in range(1,n+1):
            if num[k] == 0:
                cnt += 1
        ans.append(n-cnt)
    
    for yoko in range(W-w,W):
        for tate in range(h):

            num[b[i+tate][yoko]]+=1
            
            
    
    ANS.append(ans)
for answer in ANS:
    print(*answer)