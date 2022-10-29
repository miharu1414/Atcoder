h, w =map(int,input().split())
c =[input() for i in range(h)]
x = [0]*w

for j in range(w):
    for k in range(h):
        if c[k][j] == '#':
            x[j]+=1
print(*x)