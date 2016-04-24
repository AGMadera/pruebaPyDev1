def fib2 (n): # devuelve la serie de Fibonacci hasta n
    """Devuelve una lista conteniendo la serie de Fibonacci hasta n."""
    result = []
    c, d = 0, 1
    while c < n:
        result.append(c)
        c, d = d, c+d
    return result
        
        


a, b = 0, 1
while b < 10:

    print (b) 
    a, b = b, a+b
    
f100 = fib2(100)
f100