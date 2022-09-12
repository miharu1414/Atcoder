n,m = map(int,input().split())
s = [input() for i in range(n)]
t =  [input() for i in range(m)]

T = set()
for i in range(m):
    T.add(t[i])
import itertools
arr = list(range(n))

for i in list(itertools.permutations(arr)):
    junretu = i

    new_s = ""
    cnt = 0
    for j in range(len(junretu)):
        new_s += s[junretu[j]]
        if j != len(junretu) -1:
            new_s += "_"
            cnt += 1
    
    if new_s not in T:
        print(new_s)
        exit()
    nokori = 16-len(new_s)
    oz = [0]*(cnt-1)
    for i in range(1,nokori+1):
        oz.append(1)
        for now in itertools.permutations(oz):
            new_s = ""
            cnt = 0
            for j in range(len(junretu)):
                new_s += s[junretu[j]]
                if j != len(junretu) -1:
                    new_s += "_"
                    while len(oz)>cnt and now[cnt]:
                        new_s += "_"
                        cnt += 1
                    cnt+=1
            if new_s not in T:
                print(new_s)
                exit()
print(-1)