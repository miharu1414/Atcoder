    n = int(input())
    c = list(map(int,input().split()))

    min_c = min(c)
    waru = 0
    n_copy = n
    waru = n_copy//min_c

    ans = ""
    for i in range(waru):
        for j in range(8,-1,-1):
            if (n - min_c*(waru-i-1))>=c[j]:
                n -= c[j]
                ans+=str(j+1)
                break
    print(ans)