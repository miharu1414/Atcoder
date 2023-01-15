import sys
sys.setrecursionlimit(10**6)
n = int(input())
s,t = [], []
Before = dict()
After  = dict()
idx_Before = dict()
for i in range(n):
    a,b = map(str, input().split())
    s.append(a)
    t.append(b)
    After[a] = b
    Before[b] = a
    idx_Before[a] = i
old_name = set()
new_name = set()

for i in range(n):
    old_name.add(s[i])
    if t[i] in new_name:
        print("No")
        exit()
    new_name.add(t[i])
flag = 1
for i in range(n):
    if After[s[i]] in old_name:
        if s[i] == After[After[s[i]]]:
            flag = 0
            break
seen = [0]*n

def is_notcycle(i,new):
    if new not in old_name:
        return 1
    if seen[idx_Before[new]] == i:
        print("No")
        exit()
        return 0
    seen[idx_Before[new]] = i
    is_notcycle(i,After[new])
for i in range(n):
    if seen[i]: continue
    is_notcycle(i+1,s[i])
    
if len(new_name) == len(old_name) and new_name != old_name and flag == 1:
    print("Yes")
else:
    print("No")

