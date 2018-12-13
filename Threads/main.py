import threading
import time

class aThread(threading.Thread):
    def __init__(self, threadID, threadName, threadCounter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.threadName = threadName
        self.threadCounter = threadCounter

    def run(self):
        print("Start - ", self.threadID, self.threadName, self.threadCounter)
        self.somePrint(self.threadCounter)
        print("Stop - ", self.threadID, self.threadName, self.threadCounter)

    def somePrint(self, k):
        for i in range(k):
            print("%s: %s" % (self.threadName, time.ctime(time.time())))
            time.sleep(2)

thread1 = aThread(1, "Thread One", 5)
thread2 = aThread(2, "Thread Two", 10)

thread1.start()
thread2.start()
print("*** Some test message ***")
print(thread1.isAlive())
print(thread2.isAlive())
print("*** Another test message ***")


'''
Output:

Start -  1 Thread One 5
Thread One: Thu Dec 13 11:54:26 2018
*** Some test message ***
True
True
*** Another test message ***
Start -  2 Thread Two 10
Thread Two: Thu Dec 13 11:54:26 2018
Thread One: Thu Dec 13 11:54:28 2018
Thread Two: Thu Dec 13 11:54:28 2018
Thread One: Thu Dec 13 11:54:30 2018
Thread Two: Thu Dec 13 11:54:30 2018
Thread Two: Thu Dec 13 11:54:32 2018
Thread One: Thu Dec 13 11:54:32 2018
Thread Two: Thu Dec 13 11:54:34 2018
Thread One: Thu Dec 13 11:54:34 2018
Thread Two: Thu Dec 13 11:54:36 2018
Stop -  1 Thread One 5
Thread Two: Thu Dec 13 11:54:38 2018
Thread Two: Thu Dec 13 11:54:40 2018
Thread Two: Thu Dec 13 11:54:42 2018
Thread Two: Thu Dec 13 11:54:44 2018
Stop -  2 Thread Two 10
'''