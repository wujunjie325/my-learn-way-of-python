from Stack import *

def infixToPostifx(infixexpr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opstack = Stack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if ord(token) > 47:
            postfixList.append(token)
        elif token == "(":
            opstack.push(token)
        elif token == ")":
            topToken = opstack.pop()
            while topToken != "(":
                postfixList.append(topToken)
                topToken = opstack.pop()
        else:
            while not opstack.isEmpty():
                if prec[opstack.peek()] >= prec[token]:
                    postfixList.append(opstack.pop())
                else:
                    break
            opstack.push(token)


    while not opstack.isEmpty():
        postfixList.append(opstack.pop())


    return " ".join(postfixList)

print(infixToPostifx("1 + ( 2 * 5 ) - 6 - 3 + 1 - 6 + 6 - 7 * 2"))