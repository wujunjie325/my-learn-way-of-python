from Stack import*

def bin(n):
    res = Stack()
    while n != 0:
        res.push(n % 2)
        n = n // 2
    ans = ""
    while  not res.isEmpty():
        ans += str(res.pop())
    return ans


def baseConverter(decNuber, base):
    digits = "0123456789ABCDEF"

    remstack = Stack()
    
    while decNuber > 0:
        rem = decNuber % base
        remstack.push(rem)
        decNuber = decNuber // base
    newString = ""
    while not remstack.isEmpty():
        newString += digits[remstack.pop()]
    return newString


print(bin(10))
print(baseConverter(25, 16))
