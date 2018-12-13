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
        threadLock.acquire()
        print(self.threadName + " has acquired the Lock")
        self.somePrint(self.threadCounter)
        threadLock.release()
        print(self.threadName + " has released the Lock")
        print("Stop - ", self.threadID, self.threadName, self.threadCounter)

    def somePrint(self, k):
        for i in range(k):
            print("%s: %s" % (self.threadName, time.ctime(time.time())))
            time.sleep(2)

threadLock = threading.Lock()
threads =[]

thread1 = aThread(1, "Thread One", 3)
thread2 = aThread(2, "Thread Two", 5)
thread3 = aThread(3, "Thread Three", 4)

threads.append(thread1)
threads.append(thread2)
threads.append(thread3)

for t in threads:
    t.start()

print("*** Some test message ***")
for t in threads:
    print(t.isAlive())
print("*** Another test message ***")

'''
Output:

Without Locking:

Start -  1 Thread One 3
Thread One: Thu Dec 13 12:09:55 2018
Start -  2 Thread Two 5
Thread Two: Thu Dec 13 12:09:55 2018
*** Some test message ***
True
True
True
*** Another test message ***
Start -  3 Thread Three 4
Thread Three: Thu Dec 13 12:09:55 2018
Thread One: Thu Dec 13 12:09:57 2018
Thread Two: Thu Dec 13 12:09:57 2018
Thread Three: Thu Dec 13 12:09:57 2018
Thread One: Thu Dec 13 12:09:59 2018
Thread Two: Thu Dec 13 12:09:59 2018
Thread Three: Thu Dec 13 12:09:59 2018
Thread Three: Thu Dec 13 12:10:01 2018
Stop -  1 Thread One 3
Thread Two: Thu Dec 13 12:10:01 2018
Stop -  3 Thread Three 4
Thread Two: Thu Dec 13 12:10:03 2018
Stop -  2 Thread Two 5

With Locking:

Start -  1 Thread One 3
Thread One: Thu Dec 13 12:10:40 2018
Start -  2 Thread Two 5
*** Some test message ***
True
True
True
*** Another test message ***
Start -  3 Thread Three 4
Thread One: Thu Dec 13 12:10:42 2018
Thread One: Thu Dec 13 12:10:44 2018
Stop -  1 Thread One 3
Thread Two: Thu Dec 13 12:10:46 2018
Thread Two: Thu Dec 13 12:10:48 2018
Thread Two: Thu Dec 13 12:10:50 2018
Thread Two: Thu Dec 13 12:10:52 2018
Thread Two: Thu Dec 13 12:10:54 2018
Stop -  2 Thread Two 5
Thread Three: Thu Dec 13 12:10:56 2018
Thread Three: Thu Dec 13 12:10:58 2018
Thread Three: Thu Dec 13 12:11:00 2018
Thread Three: Thu Dec 13 12:11:02 2018
Stop -  3 Thread Three 4
'''