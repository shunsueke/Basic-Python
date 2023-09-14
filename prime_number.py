a = input("aの値を入力してください")
b = input("bの値を入力してください")

 # To Do

A = int(a)

def controller (X):

    if  X <= 0:
        return False
    elif type(X) != int:
        return False
    else:
        if X == 1:
            print(X,"は素数ではないです")

        elif X == 2:
            print(X,"は素数です")
        
        else:
            count = 2
            while count <= X-1:
                c = X % count
                if c == 0:
                   print(X,"は素数ではありません")
                   break
                else:
                  count += 1
                  if count == X-1:
                    print(X,"は素数です")
                    break
        

controller(A)

    