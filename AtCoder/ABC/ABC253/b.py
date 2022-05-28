h,w = map(int,input().split())
s = [input() for i in range(h)]

count = 0
for i in range(h):
    for j in range(w):
        if s[i][j] == 'o' and count==0:
            x,y = i,j
            count = 1
        elif s[i][j] == 'o':
            print(abs(x-i)+abs(y-j))
            exit()
