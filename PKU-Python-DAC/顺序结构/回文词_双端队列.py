from queue import deque

def palchecker(a_String):
    chardeque = deque()
    for ch in a_String:
        chardeque.append(ch)

    flge = True

    while len(chardeque) > 1 and flge:

        flge = chardeque.pop() == chardeque.popleft()

    return flge

print(palchecker("123454321"))