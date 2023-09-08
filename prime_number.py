a = input("aの値を入力してください")

 # To Do

A = int(997)


def controller (X):
      
    if X == 1:
      print(X,"は素数ではありません")

    elif X == 2 :
      print(X,"は素数です")
    
    elif X == 3:
       print(X,"は素数です")

    else:
       count = 2
       while count <= X -1:
          c = X % count 
          if c == 0:
             print(X,"は素数ではありません")
             break
          else:
             count += 1 
             if count == X -1:
                print(X,"は素数です")
                break


controller(A)