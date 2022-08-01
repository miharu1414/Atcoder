n,a,b = map(int,input().split())
p,q,r,s = map(int,input().split())

ans  =[]
width = s-r+1
height = q - p + 1
for i in range(height):
    S = []
    for j in range(width):
        S.append('.')
    ans.append(S)


kouho = max(1-a,1-b)
kouho2 = min(n-a,n-b)
minx = a+kouho
miny = b+kouho
maxx =a+kouho2
maxy = b + kouho2

for i in range(height):
    for j in range(width):
        if j + r >= miny and j + r <= maxy:

            if i + p >= minx and i + p <= maxx:
                ans[i][j]  = "#"
for s in ans:
    print(s)