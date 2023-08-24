# TODO
e = 1
a = 1 + e
b = 1

while True:
    e = e / 2
    a = 1 + e
    b = 1
    if a - b == 0:
        print(2*e)
        break