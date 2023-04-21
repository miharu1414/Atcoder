n = int(input())
q = int(input())
Num = [[] for i in range(2*(10**5)+1)]
Box = [[] for i in range(n+1)]
import collections

d = collections.defaultdict(set)
for i in range(q):
    query = list(map(int,input().split()))
    idx = query[0]
    if idx == 1:
        Box[query[2]].append(query[1])
        if query[2] not in Num[query[1]]:
            Num[query[1]].append(query[2])
            


        d[query[1]].add(query[2])
    elif idx == 2:
        Box[query[1]].sort()
        print(*Box[query[1]])
    else:
        Num[query[1]].sort()
        print(*Num[query[1]])
    