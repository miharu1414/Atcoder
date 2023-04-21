h, w = map(int,input().split())
a = [list(map(int,input().split())) for i in range(h)]

def alpha(x):
    if x==0:
        return '.'
    return chr(ord('A')+x-1)
ans = []
for i in range(h):
    s = ''
    for j in range(w):
        s += alpha(a[i][j])
    ans.append(s)
    print(s)
    