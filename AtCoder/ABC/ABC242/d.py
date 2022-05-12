from re import X


s = input()
q = int(input())
for i in range(q):
    t,k = map(int,input().split())
    x = k// 2**t
    k %= 2**t