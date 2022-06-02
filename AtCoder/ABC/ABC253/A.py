a,b,c = map(int,input().split())
import statistics

lst = [a,b,c]

if b == statistics.median(lst):
    print("Yes")
else:
    print("No")