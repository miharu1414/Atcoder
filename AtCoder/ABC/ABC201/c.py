s = input()



maru = 0
batu = 0
kanri = [0]*10
O = set()
X = set()
hatena = set()
num = [0]*10
for i in range(10):
    if s[i]=='o':
        kanri[i] = 1
        maru +=1
        num[i] = 1
        O.add(i)
    elif s[i] == 'x':
        kanri[i] = 0
        batu += 1
        num[i] = -9999
        X.add(i)
    else:
        kanri[i] = -1
        num[i] = 0
        hatena.add(i)
if maru > 4:
    print(0)
    exit()
    
dp = [[0]*10 for i in range(5)]


def check(a,b,c,d):
    kind = set()
    if a in X or b in X or c in X or d in X:
        return False


    if a in O:
        kind.add(a)
    if b in O:
        kind.add(b)
    if c in O:
        kind.add(c)
    if d in O:
        kind.add(d)
    if len(kind) == maru:
        return True
    return False
ans = 0
    
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                if check(i,j,k,l):

                    ans += 1
print(ans)
            
                