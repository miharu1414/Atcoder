
x = float(input())
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN

# 整数で丸め
a = Decimal(str(x)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
print(a)