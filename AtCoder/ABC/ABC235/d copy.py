
a,n = map(int,input().split())


from collections import deque 
q = deque()
m = 10**int(len(str(n)))
d = [-1]*m

d[1] = 0 
q.append(1)

while len(q):
    c = q.popleft()
    cnt = d[c]

    op1 = a * c
    if op1 < m and d[op1] == -1:
        d[op1] = cnt + 1
        q.append(op1)
    
    if c>= 10 and c %10 != 0:
        s = str(c)
        op2 = int(s[-1] + s[:-1])
        if op2 < m and d[op2] == -1:
            d[op2] = cnt + 1
            q.append(op2)
print(d[n])
