from re import L


v,a,b,c = map(int,input().split())
while 1:
    if v - a < 0:
        print("F")
        exit(0)
    v -= a
    
    if v  - b < 0:
        print("M")
        exit(0)
    v -= b
    if v - c < 0:
        print("T")
        exit(0)
    v -= c