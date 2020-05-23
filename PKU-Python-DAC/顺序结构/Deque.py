class Deque():

    def __init__(self):
        self.items = []

    def is_Empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def addFrount(self, item):
        self.items.append(item)
    
    def addRear(self, item):
        self.items.insert(0, item)
    
    def removeFront(self):
        self.items.pop()

    def removeRear(self):
        self.items.pop(0)


