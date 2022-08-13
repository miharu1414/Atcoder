r,c = map(int,input().split())

g = [[0]*15 for i in range(15)]
dif = max(abs(r-8),abs(c-8))
if dif%2:
    print("black")
else:
    print("white")