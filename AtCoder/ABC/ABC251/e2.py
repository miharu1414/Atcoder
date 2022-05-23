from re import I


n = int(input())
a = list(map(int,input().split()))

select = dict()
num = []
fore_back = 0
point = []

fore_back = 1
pair = []
for i in range(n):
    pair.append([a[i],i,i+1])

    