from queue import Queue
import random

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm # 打印速度
        self.currentTask = None #打印任务
        self.timeRemaining = 0 #任务倒计时

    def tick(self):#处理打印以秒为单位
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None
        
    def busy(self):#判断是否有任务在打印
        if self.currentTask != None:
            return True
        return False
    
    def startNext(self, newtask):#打印下一个任务
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate


class Task:#初始化任务
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)


    def getStamp(self):
        return self.pages

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def newPrintTask():#产生打印任务
    num = random.randrange(1,181)
    if num == 1:
        return True
    return False


def simulation(numseconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)
    printqueue = Queue()
    waittingtimes = []
    for currentSecond in range(numseconds):
        if newPrintTask():
            task = Task(currentSecond) #创建任务并给出该进入队列的时间
            printqueue.put(task) #入队
            #print(printqueue.empty(),print(printqueue.qsize()))
        if (not labprinter.busy()) and not printqueue.empty(): # 如果有任务且打印机为空闲状态
            nexttask = printqueue.get() # 从队列中取出任务
            waittingtimes.append(nexttask.waitTime(currentSecond))# 计算该任务的等待时间
            labprinter.startNext(nexttask) # 讲任务从队列加入打印机
            
        labprinter.tick() #机器打印一秒
    return sum(waittingtimes) / len(waittingtimes)

def main():
    for i in range(10):
        print("avg wait %.2f secs"%(simulation(3600, 10)))


if __name__ == "__main__":
    main()
