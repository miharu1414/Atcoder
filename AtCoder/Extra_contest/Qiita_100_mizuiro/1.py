while 1:
    n,x = map(int,input().split())
    if  n==0 and x == 0:
        break

    ans = 0
    
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if (i+1) + (j+1) + (k+1) == x:
                    ans += 1
    print(ans)
                