class Node(object):
    def __init__(self, date, next = None):
        self.date = date
        self.next = next



class Single_link_list(object):
    def __init__(self, head = None):
        self.head = head


    def add(self,item):
        node = Node(item)
        node.next = self.head
        self.head = node


    def append(self, item):
        node = Node(item)
        cur = self.head
        if cur == None:
            self.add(item)
        else:
            while cur.next != None:
                cur = cur.next
            cur.next = node
    def trivel(self):
        cur = self.head
        print(cur.date,end = " ")
        while cur.next != None:
            cur = cur.next
            print(cur.date,end = " ")
        print()


    def insert(self, item, position):
        if position == 0:
            self.add(item)
        elif position > self.length():
            self.append(item)
        else:
            node = Node(item)
            count = 1
            cur = self.head
            while count < position:
                cur = cur.next
                count += 1
            node.next = cur.next
            cur.next = node


    def length(self):
        count = 0
        cur = self.head
        while cur != None:
            cur = cur.next
            count += 1
        return count


    def delect(self, position):
        if position == 0:
            self.head = self.head.next
        if position > self.length:
            pass
a = Node(10)
lb = Single_link_list(a)

for i in range(1,10):
    lb.append(i)

lb.trivel()
lb.insert(15,1)
lb.trivel()
print(lb.length())