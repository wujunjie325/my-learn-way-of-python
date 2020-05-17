from Stack import *
s = Stack()

s.push(4)
print(s.isEmpty())
s.push("dog")
print(s.pop())
print(s.size())
for i in range(1, 10):
    s.push(i)
print(s.peek())
print(s.size())
print(s.pop())