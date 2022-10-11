n = int(input())
xy = [map(int,input().split()) for i in range(n)]
x,y = [list(i) for i in zip(*xy)]



from collections import defaultdict
from operator import ne


x_search = defaultdict(list)
y_search =  defaultdict(list)

sonzai = dict()

for i in range(n):
    x_search[x[i]].append(i)
    y_search[y[i]].append(i)
    sonzai[(x[i],y[i])] = 1
ans = 0
for i in range(n):
    X = x[i]
    Y = y[i]
    for next_x in x_search[X]:
        if y[next_x] <= Y:
            continue
        for next_y in y_search[Y]:
            if x[next_y] <= X:
                continue
            if (x[next_y],y[next_x]) in sonzai:
                ans += 1
            
print(ans)