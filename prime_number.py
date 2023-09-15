a = input("aの値を入力してください")
b = input("bの値を入力してください")

 # To Do

A = 14

def controller (X):

    if  X <= 0:
        return  False
    elif type(X) != int:
        return  False
    
    else:
        if X == 1:
          return False

        for i in range(2,int(X**0.5) + 1):
           if X % i == 0:
            return False
        return True
                                   
controller(A)        

    