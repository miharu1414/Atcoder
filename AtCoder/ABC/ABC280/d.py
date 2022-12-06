def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
k = int(input())

soinsuu = factorization(k)
num = []
for k in range(len(soinsuu)):
    
    now = soinsuu[k][0]
    left = soinsuu[k][1]
    pos = []
    be = 0
    Sum = 0
    
    for i in range(left):
        x = now*(i+1)
        original = x
        cnt= 0
        while x%now == 0 and x // now >0:
            cnt += 1
            x //= now
        pos.append([original,cnt])
    for i in range(len(pos)):
        if left <= Sum + pos[i][1]:
            num.append(pos[i][0])

            break
        Sum += pos[i][1]
        

print(max(num))