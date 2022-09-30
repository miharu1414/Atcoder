

n = int(input())
def dec2bin(target):
    amari = []
    while target:
        amari.append(target%2)
        target = target//2
    amari.reverse()
    return amari

N = dec2bin(n)


L = len(N)

def make(array):
    ans = 0
    i = 0
    while len(array) > i:
        ans = (ans*2)+array[i]
        i+=1
    return ans
def rec(length,array):
    if length==0:
        print(make(array))

        return 0
    
    if N[L-length] == 0:
        array.append(0)
        rec(length-1,array)
        array.pop(-1)


    else:    
        array.append(0)
        rec(length-1,array)
        array.pop(-1)
        array.append(1)
        rec(length-1,array)
        array.pop(-1)

array = []
rec(L,array)