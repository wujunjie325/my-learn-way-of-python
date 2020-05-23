class Node(object):

    def __init__(self, item, next = None):
        self.data = item
        self.next = next

    def getData(self):
        return self.data

    def getNext(self):
        return self.next
    
    def setData(self, item):
        self.data = item
    
    def setNext(self, node):
        self.next = node


class Link_list(object):

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def append(self, data):
        node = Node(data)
        cur = self.head
        if cur is None:
            self.head = node
        else:
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def travel(self):
        cur  = self.head
        while cur is not None:
            print(cur.data,end=" ")
            cur = cur.getNext()
        print()
    
    def size(self):
        cur  = self.head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.getNext()
        return count
    
    def search(self, item):
        cur = self.head
        while cur is not None:
            if cur.getData() == item:
                return True
            cur = cur.getNext()
        return False

    def remove(self, item):
        cur = self.head
        if cur.getData() == item:
            self.head = cur.getNext()
        else:
            while cur.getNext() is not None:
                if cur.getNext().getData() == item:
                    cur.setNext(cur.getNext().getNext())
                    break
    
    def pop(self, pos):
        cur = self.head
        if pos == 0:
            temp = self.head.getData()
            self.head = self.head.getNext()
            return temp
        else:
            cur = self.head
            count = 1
            while cur.getNext() is not None and count != pos:
                cur = cur.getNext()
                count += 1
            temp = cur.next.getData()
            cur.setNext(cur.getNext().getNext())
            return temp

    def insert(self, pos, item):
        if pos == 0:
            self.add(item)
        else:
            node = Node(item)
            count = 0
            cur = self.head
            while count + 1 < pos and cur.getNext() is not None:
                cur = cur.getNext()
                count += 1
            node.setNext(cur.next)
            cur.setNext(node)


a = Link_list()
for i in range(10):
    a.append(i)
a.travel()
print(a.size())
a.remove(1)
a.add(10)
print(a.size())
a.remove(0)
a.travel()
print(a.pop(0),"this is a pop method")
a.travel()
a.insert(0, 8)
a.travel()
a.insert(3, 12)
a.travel()
a.insert(a.size()-1, 666)
a.insert(a.size()+20, 786)
a.travel()
a.remove(8)
a.insert(2,8)
a.insert(5,8)
a.travel()
print(a.search(8))
print(a.search(1))