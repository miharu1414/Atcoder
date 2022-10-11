n,a,b = map(int,input().split())
p,q,r,s = map(int,input().split())

tate,yoko  = q-p+1,s-r+1
start_x,start_y = a-p,b-r
color = [[0]*(yoko) for i in range(tate)]
def func1(x,y):
    if x - start_x == y - start_y:
        return True
    return False
def func2(x,y):
    if x - start_x == -(y - start_y):
        return True
    return False

for i in range(tate):
    for j in range(yoko):
        if func1(i,j) or func2(i,j):
            color[i][j] = 1
ans = []
for i in range(tate):
    s = ""
    for j in range(yoko):
        if color[i][j] == 1:
            s+='#'
        else:
            s+='.'
    ans.append(s)
for i in range(tate):
    print(ans[i])
    
