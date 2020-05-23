class Node(object):
    def __init__(self, item):
        self.data = item
        self.next = None


class Orderedlist(object):
    
    def __init__(self):
        self.head = None
        self.lenth = 0

    def __gt__(self,item):
        return self.data > item

    def add(self, item):
        self.lenth += 1
        node = Node(item)
        cur = self.head
        if self.head is None:
            self.head = node
        elif cur.data > item:
            node.next = cur
            self.head = node
        else:
            while cur.next is not None and cur.next.data < item:
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def isEmpty(self):
        return self.head is None

    def travel(self):
        cur = self.head
        while cur is not None:
            print(cur.data,end = " ")
            cur = cur.next
        print()

    def size(self):
        return self.lenth
    
    def remove(self, item):
        cur = self.head
        if cur is not None:
            if cur.data == item:
                self.head = cur.next
                self.lenth -= 1
            else:
                while cur.next is not None:
                    if cur.next.data == item:
                        cur.next = cur.next.next
                        self.lenth -= 1
                        return
                    cur = cur.next

    def search(self, target):
        cur = self.head
        while cur is not None and  target < cur.data:
            if cur.data == target:
                return True
        return False

a = Orderedlist()
a.add(10)
a.add(20)
a.add(15)
a.add(17)
a.add(6)
a.add(30)
a.travel()
print(a.size())
a.remove(17)
a.travel()