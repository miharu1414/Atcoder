s = input()

numState = [[0]*10 for i in range(len(s)+1)]
from collections import defaultdict

stateDict = defaultdict(list)

stateDict[tuple(numState[0])] = 1
for i in range(len(s)):
    numState[i+1] =  numState[i]
    numState[i+1][int(s[i])] = ~numState[i][int(s[i])]
    if tuple(numState[i+1]) not in stateDict:
        stateDict[tuple(numState[i+1])] = 1
    else:
        stateDict[tuple(numState[i+1])] += 1

ans = 0
for k,v in stateDict.items():
    ans += v*(v-1)//2
print(ans)
    
    


    
    

