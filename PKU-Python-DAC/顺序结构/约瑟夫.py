from queue import Queue

def ysf(namelist, num):
    queue = Queue()
    for name in namelist:
        queue.put(name)
    index = 0
    while queue.qsize() > 1:
        #print(queue.qsize())
        index += 1
        if index != num:
            queue.put(queue.get())
        else:
            #print(queue.queue,"cs")
            queue.get()
            index = 0
    return queue.get()

    
a = [1,2,3,4]
print(ysf(a, 3))
print(ysf_2(a, 3))
