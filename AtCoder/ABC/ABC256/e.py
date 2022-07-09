n = int(input())
x = list(map(int,input().split()))
c = list(map(int,input().split()))
for i in range(n):
    x[i] -= 1
cost = [0]*n
for i in range(n):
    cost[x[i]] += c[i]

