x = 4
y = 6

def GCD(a, b):
    if(b == 0):
        return abs(a)
    else:
        return GCD(b, a % b)
 
GCD(x, y)