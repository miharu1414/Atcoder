n  = int(input())

def Count_div(x):
    count = 0

    i = 1
    while i * i <= x:
        if x%i == 0:
            count+=2
        if x == i*i:
            count-=1
        i+=1 

    return count


ans = 0
for i in range(1,n+1,2):

    if Count_div(i)==8:
        ans+=1
print(ans)