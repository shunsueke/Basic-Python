a = input("a の値を入力: ")
b = input("b の値を入力: ")

# TODO
A = int(a)
B = int(b)

if A < B:
    A,B = B,A
print(A,B)

r = A % B 

if r == 0:
    print(B)

else:
  while True:
    A = B
    B = r
    r = A % B
    if r ==0:
        print(B)
        break
