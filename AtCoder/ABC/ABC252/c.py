n = int(input())
s = [input() for i in range(n)]

count = [0]*10

for j in range(10):
    j_pos = [0]*10
    max_k = 0
    for i in range(n):
        for k in range(10):
            if s[i][k] ==str(j):
                j_pos[k]+=1
                if max_k < k:
                    max_k = k
    boolen = 1
    max_kaburi = 1
    max_key = 0
    for l in range(10):
        if j_pos[l]>1:
            if max_kaburi <= j_pos[l]:
                max_kaburi = j_pos[l]
                max_key = l

            boolen = 0
    if boolen:
        count[j] = max_k
    else:
        count[j] = (max_kaburi-1)*10 + max_key

print(min(count))
            