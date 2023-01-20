h, w, k = map(int,input().split())
c = [input() for i in range(h)]

h_n = [i for i in range(h)]
w_n = [i for i in range(w)]
default_cnt = 0
for i in range(h):
    for j in range(w):
        if c[i][j] == '#': default_cnt+=1
import itertools
ans = 0

for i in range(h+1):
    
    for l_h in itertools.combinations(h_n,i):
        for j in range(w+1):
            for l_w in itertools.combinations(w_n,j):
                cnt = 0
                seen = [[0]*w for i in range(h)]
                for idx in l_h:
                    for j_ in range(w):
                        seen[idx][j_] = 1
                        if c[idx][j_] == '#':
                            cnt += 1
                for jdx in l_w:
                    for i_ in range(h):
                        if c[i_][jdx] == '#' and seen[i_][jdx] == 0:
                            cnt += 1
                if default_cnt - cnt == k: ans += 1
print(ans)

                                
                