n = int(input())
h = list(map(int,input().split()))
max  = max(h)
for i in range(n):
    if max == h[i]:
        print(i+1)
        exit()
         