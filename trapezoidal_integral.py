from math import sin,pi,sqrt,exp
# --example--
# print(sin(0))
# >>> 0
# -----------

def integral(f ,a = 0,b = 1,n = 100):
    h = (b - a) / n
    s = 0
    for i in range(1,n):
        s +=  (h/2)*(f(a+(i-1)*h) + f(a+i*h))
    return s
        

print(integral(f=sin,a =0,b=pi/2,n=50))
print(integral(f= lambda x: 4/(1+x**2)))
print(integral(f= lambda x:sqrt(pi)*exp(-x**2), a =-100 ,b=100, n=1000))
    