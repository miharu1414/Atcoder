n, q = map(int,input().split())
a = list(map(int,input().split()))
shift = 0
for i in range(q):
    t,x,y= map(int,input().split())
    x -= 1
    y -= 1
    if x - shift<0:
        real_x = n - (x-shift)%n
    else:
        real_x = x - shift

    if y - shift<0:
        real_y = n - (y-shift)%n
    else:
        real_y = y - shift

    if t == 1:
        sub = a[real_x]
        a[real_x] = a[real_y]
        a[real_y] = sub

    elif t == 2:
        shift += 1

    else:
        print(a[real_x])
    