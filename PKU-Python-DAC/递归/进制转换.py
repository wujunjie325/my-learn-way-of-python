def toStr(n, base):
    converrString = "0123456789ABCDEF"
    if n < base:
        return converrString[n]
    return toStr(n // base, base) + converrString[n % base]
