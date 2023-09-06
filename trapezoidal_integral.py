from math import sin
from math import pi
# --example--
# print(sin(0))
# >>> 0
# -----------

a = input("a の値を入力: ")
b = input("b の値を入力: ")

A = int(10)
B = int(23)

def controller (X):
    count = 2
    while count  <= X -1:
        c = X % count 
        count  += 1
        if c == 0:
            print(X,"は素数でありません")
            break
        else:
            print(X,"は素数です")
            break

controller(A)

controller(B)
