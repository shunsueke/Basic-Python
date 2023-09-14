a = int(input("a の値を入力: "))
b = int(input("b の値を入力: "))

# TODO
    
A = int(6)
B = int(12)

def Definition(X,Y):
 
 if X <= 0 or  Y <= 0:
   return False
 
 elif type(X) != int or type(Y) != int:
   return False
 
 else:
  if X < Y:
   X,Y = Y,X

  r = X % Y    
  if r == 0:
   print(Y)
  else:
   while True:
    X = Y
    Y = r
    r = X % Y
    if r ==0:
        print(Y)
        break

def Which_one(X,Y):
  if Definition(X,Y) == 1:
    return True
  else:
    return False
  
print(Definition(A,B))
print(f"A,Bは互いに素である。{Which_one(A,B)}")


