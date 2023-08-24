a = input("aの値を入力してください")
b = input("bの値を入力してください")

 # To Do

A = int(a)
B = int(b)

count = 2

while count <= A-1:
    c = A % count 
    count += 1
    if c == 0:
        print(A,"は素数です")
        break
    else:
        print(A,"は素数ではありません")
        break

while count <= B-1:
    d = B % count 
    count += 1
    if d == 0:
        print(B,"は素数です")
        break
    else:
        print(B,"は素数ではありません")
        break
    