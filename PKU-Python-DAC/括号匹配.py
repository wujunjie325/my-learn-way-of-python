from Stack import *

def parChecker_1(symbol):#圆括号匹配
    stack = Stack()
    for i in symbol:
        if i == '(':
            stack.push(i)
        else:
            if stack.isEmpty():
                return False
            else:
                stack.pop()
    if stack.isEmpty():
        return True
    return False


def parChecker_2(symbol):#各种括号匹配
    stack = Stack()
    assist = {')':'(', ']':'[', '}':'{'}
    for i in symbol:
        if i in '({[':
            stack.push(i)
        else:
            if stack.isEmpty() or stack.pop() != assist[i]:
                return False
    if stack.isEmpty():
        return True
    return False

a = '([]){}()([)'
print(parChecker_2(a))
