from Stack import *

def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            a = operandStack.pop()
            b = operandStack.pop()
            operandStack.push(do_math(token, b, a))
    return operandStack.pop()


def do_math(op, op1, op2):
    if op == "+":
        return op1 + op2
    elif op == "-":
        return op1 - op2
    elif op == "*":
        return op1 * op2
    else:
        return op1 / op2

x = "1 2 + 3 *"
print(postfixEval(x))
