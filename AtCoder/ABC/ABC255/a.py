r,c = map(int,input().split())
a = []
for i in range(2):
    x,y = map(int,input().split())
    a.append(x)
    a.append(y)
print(a[(c-1)+2*(r-1)])