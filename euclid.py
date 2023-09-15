a = (input("a の値を入力: "))
b = (input("b の値を入力: "))

# TODO
    
A = 100
B = 2

def Definition(X,Y):
 
 if X <= 0  or  Y <= 0:
   return False
 
 elif type(X) != int or type(Y) != int:
   return False
 
 else:
  if X < Y:
   X,Y = Y,X

  r = X % Y    
  if r == 0:
    return Y
  else:
    while r != 0:
     X,Y = Y,r
     r = X % Y
    return Y

def Which_one(X,Y):
  if Definition(X,Y) == 1:
    return True
  else:
    return False
  
print(Definition(A,B))
print(f"A,Bは互いに素である。{Which_one(A,B)}")

