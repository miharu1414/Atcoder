n = int(input())
t = input()
from collections import deque

d = deque()
fo = deque()
ba =deque()
rev = deque()
for i in range(n):
    rev.appendleft(t[i])
for i in range(n,2*n):
    ba.append(t[i])
for i in range(1,n+1):
    new = fo + ba
    