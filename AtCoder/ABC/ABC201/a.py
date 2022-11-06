a = list(map(int,input().split()))
import itertools
for i in list(itertools.permutations(a)):
    for j in range(3):
        if i[2] - i[1] == i[1] - i[0]:
            print("Yes")
            exit()
else:
    print("No") 
