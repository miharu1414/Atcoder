n, k = map(int,input().split())
a = list(map(int,input().split()))
q = int(input())
lr = [map(int,input().split()) for i in range(q)]
l,r = [list(i) for i in zip(*lr)]

Ruiseki = [0]*n
for i in range(n):
    