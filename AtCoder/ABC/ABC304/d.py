w, h = map(int,input().split())
n = int(input())

pq = [map(int,input().split()) for i in range(n)]
p,q = [list(i) for i in zip(*pq)]

A = int(input())
a = list(map(int,input().split()))
B = int(input())
b = list(map(int,input().split()))
a.append(w)
b.append(h)
import bisect
group = dict()
for i in range(n):
    former = bisect.bisect_left(a,p[i])
    latter = bisect.bisect_left(b,q[i])
    if (former,latter) not in group:
        group[(former,latter)] = 1
    else:
        group[(former,latter)] += 1

min_value = 10**15
max_value = -10**15

for k,i in group.items():
        if group[k] < min_value:
            min_value = group[k]
        if group[k] > max_value:
            max_value = group[k]
if len(group) < (A+1)*(B+1):
    min_value = 0
print(min_value,max_value)
    

