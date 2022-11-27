a, b  = map(int,input().split())


import math
def f(x):
    return a / math.sqrt(x+1) + b * x 

def binary_search(x,y):
    left = 0
    right = 10**18+1
    
    while left<right-1:
        middle = (left + right) // 2
        if f(left) > f(right):
            left = middle 
        elif f(left) == f(right):
            left = middle -1
        else:
            right  = middle 
    return left

print(f(binary_search(a,b)))
        
        