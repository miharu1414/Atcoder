x,y,a,b = map(int,input().split())

st = x
ex = 0
i = 0
while a * st < st + b and a*st < y:
    st *=a
    i += 1
j = (y-1 - st)//b
print(i+j)


