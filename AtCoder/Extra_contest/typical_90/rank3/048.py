# https://atcoder.jp/contests/typical90/tasks/typical90_av

n, k = map(int,input().split())
a = []
b = []
score = []
for i in range(n):
    x, y = map(int,input().split())
    a.append(x)
    b.append(y)
    score.append(y)
    score.append(x-y)

score.sort(reverse=True)
count = 0
for i in range(k):
    count += score[i]
print(count)