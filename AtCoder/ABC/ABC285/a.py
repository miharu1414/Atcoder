a,b = map(int,input().split())

if a*2 == b or a*2 + 1 == b or b * 2 == a or b*2 + 1== a:
    print("Yes")
else:
    print("No")