n = int(input())
h = list(map(int,input().split()))
now = 0
height = h[0]
for i in range(1,n):
    if h[i] > height:
        height = h[i]
        now = i
    else:
        break
print(height)