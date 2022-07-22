x1,y1,x2,y2 = map(int,input().split())

x = [2,1,-1,-2,-2,-1,1,2]
y = [1,2,2,1,-1,-2,-2,-1]

for dx,dy in zip(x,y):
    nowx = x1+dx
    nowy = y1+dy

    dis = (nowx - x2)**2 + (nowy-y2)**2
    if dis == 5:
        print("Yes")
        exit()
print("No")