a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
A = int(a)
B = int(b)

if A < B:
    temp = A
    A = B
    B = temp 

r = A % B    

while True:
    A = B
    B = r
    r = A % B
    if r ==0:
        print(B)
        break
