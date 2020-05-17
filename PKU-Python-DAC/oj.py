a = input()
stack = []
i = 0
j = 0


while j < 10 and i <= 10:
    stack.append(j)
    j += 1
    while stack != [] and i == stack[-1]:
        stack.pop()
        i += 1
print(stack)
if stack == []:
    print("Yes")
else:
    print("No")