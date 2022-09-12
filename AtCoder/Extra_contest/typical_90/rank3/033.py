h,w = map(int,input().split())
count = 0
count = int((h+1)//2) * int((w+1)//2 )
if h==1 or w ==1:
    print(h*w)
else:
    print(count)