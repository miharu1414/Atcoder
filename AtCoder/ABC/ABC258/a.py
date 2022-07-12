k = int(input())
hour = 21 + k//60
min= k%60
min = str(min).zfill(2)
print(f'{hour}:{min}')