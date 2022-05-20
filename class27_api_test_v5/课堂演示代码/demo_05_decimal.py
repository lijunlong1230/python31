print( 0.1 + 0.2 == 0.3)
print(0.1+0.2, 0.2+0.3, 0.1+0.3, 0.2+0.2)
# 浮点数的精确运算， Decimal
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))