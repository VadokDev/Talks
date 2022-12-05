def GCD(x , y):
    if y == 0:
        return x
    r = int(x % y)
    return GCD(y , r)
