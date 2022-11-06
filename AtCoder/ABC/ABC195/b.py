from cmath import inf


a,b,w = map(float,input().split())

mina = inf
maxa = -1
w *= 1000

x = w //a
y = w/b
import math

if int(y)*b < w and a * math.ceil(y)>w:
    print("UNSATISFIABLE") 
else:
    print(math.ceil(y),int(x))
