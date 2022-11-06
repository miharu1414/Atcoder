
n = int(input())
a = list(map(int,input().split()))

T = dict()

cnt = 0
root = [-1]*(2*10**5+1)
for i in range(2*10**5+1):
    root[i]= i
    T[i] = i

                

print(cnt)