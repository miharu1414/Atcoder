n,s,d  = map(int,input().split())
xy = [map(int,input().split()) for i in range(n)]
x,y = [list(i) for i in zip(*xy)]
for i in range(n):
    if x[i] < s and y[i] > d:
        print("Yes")
        exit()
print("No")