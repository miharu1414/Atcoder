h1,w1  = map(int,input().split())
a = [list(map(int,input().split())) for i in range(h1)]
h2, w2 = map(int,input().split())
b = [list(map(int,input().split())) for i in range(h2)]

import itertools
l = [i for i in range(h1)]
r = [i for i in range(w1)]
c = itertools.combinations(l, h2)


pos = 0

last = [[0] * w2 for i in range(h2)]
for v in c:

    new = []
    for i in v:
        new.append(a[i])


    d = itertools.combinations(r,w2)
    for k in d:
        posj = 0
        for j in k:
            for i in range(len(new)):
                last[i][posj] = new[i][j]
            posj += 1

        if last == b:
            pos = 1
if pos:
    print("Yes")
else:
    print("No")