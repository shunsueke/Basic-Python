from math import sin
from math import pi
# --example--
# print(sin(0))
# >>> 0
# -----------
a = 0
b = pi/2
h = (b - a) / 100
k = 1
q = 0.0

while k <= 100:
    p = (h/2)*(sin(a+(k-1)*h) + sin(a+k*h))
    q = p + q
    k = k + 1
    
print(q)