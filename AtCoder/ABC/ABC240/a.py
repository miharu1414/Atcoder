a, b = map(int,input().split())
if b  == 10:
    if a == 9 or a == 1:
        print("Yes")
    else:
        print("No")
else:
    if a == b-1:
        print("Yes")
    else:
        print("No")