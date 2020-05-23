class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, date):
        self.items.append(date)


    def pop(self):
        return self.items.pop()


    def size(self):
        return len(self.items)


    def isEmpty(self):
        return self.items == []


    def peek(self):
        return self.items[-1]