a, b, x = map(int,input().split())


left = 0
right = 10**9+1

def price(n):
    global a,b
    return a*n+b*len(str(n))

while right - left > 1:
    mid = (right+left)//2
    
    if price(mid) > x:
        right = mid
    else:
        left = mid
print(left)
    