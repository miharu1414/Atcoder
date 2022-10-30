a,b,c = map(int,input().split())
if c == 0:
    a -= 0.5
    if a > b:
        print("Takahashi")
    else:
        print("Aoki")
else:
    b -= 0.5
    if a > b:
        print("Takahashi")
    else:
        print("Aoki")