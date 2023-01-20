n = int(input())
s = input()
q = int(input())
tab = [map(int,input().split()) for i in range(q)]
t, a, b = [list(i) for i in zip(*tab)]

String_idx = []*(2*n)
for_s = []
back_s = []
for i in range(n):
    for_s.append(s[i])
    back_s.append(s[n+i])
