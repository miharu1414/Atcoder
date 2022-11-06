n = int(input())
import math
i  = math.sqrt(2*n)

for j in range(int(i),10**6,1):
    if (j+1)*j>=2*n:
        print(j)
        break