n ,a, b= map(int,input().split())
boole1 = 1
boole2 = 1
for i in range(n*a):
    if i %a ==0 and i !=0:
        boole1 *= -1
    s = ''
    if boole1 == 1:
        boole2 = 1
    else:
        boole2 =-1
    for j in range(n*b):
       
        if j %b ==0 and j != 0:
            boole2 *= -1
        if boole2 == 1:
            s+= "."
        else:
            s+='#'
    print(s)
