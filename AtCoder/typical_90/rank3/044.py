

n,q = map(int,input().split())
a = list(map(int,input().split()))


shift = 0
for i in range(q):
    t,x,y = map(int,input().split())

    shift_1 = shift
    shift_2 = shift

    x-=1
    y-=1

    if x-shift_1<0:
        x =n - (shift_1-x)%n
        if x ==n:
            x= 0
    else:
        x-=shift_1
    
    if yqsd -shift_2 <0:
        y =n - (shift_2-y)%n 
        if y ==n:
            y= 0
    else:
        y-=shift_2

    if t==1:
        sub = a[x]
        a[x] = a[y]
        a[y] = sub

    elif t ==2:
        shift+=1
    else:
        print(a[x])