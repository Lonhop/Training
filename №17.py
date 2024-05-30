def f(a,b):
    if a>b or a==20 or a==25: return False
    if a==b: return True
    return f(a+1,b)+f(a*2,b)+f(a**2,b)
print(f(2,15)*f(15,35)*f(35,50))
