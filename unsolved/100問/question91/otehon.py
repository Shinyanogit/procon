import math

a, b, x = map(int, input().split())
if x < a**2 * b / 2:
    y = 2 * x / (a * b)
    print(math.degrees(math.atan(b / y)))
else:
    y = 2 * (b - x / (a**2))
    print(math.degrees(math.atan(y / a)))
