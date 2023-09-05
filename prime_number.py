a = input("aの値を入力してください")
b = input("bの値を入力してください")

 # To Do

A = int(a)
B = int(b)

count = 2

def controller (X):
    while count  <= X -1:
        c = X % count 
        count  += 1
        if c == 0:
            print(X,"は素数です")
            break
        else:
            print(X,"は素数でありません")
            break

controller(A)

controller(B)
    