import threading
import time

class thread_WriteInFile(threading.Thread):
    def __init__(self, strToWrite, outFile):
        threading.Thread.__init__(self)
        self.strToWrite = strToWrite
        self.outFile= outFile

    def run(self):
        f = open(self.outFile, "a")
        f.write(self.strToWrite+"\n")
        f.close()
        time.sleep(2)

def Main():
    str = input("Enter a string to write it in a file:")
    writingThread = thread_WriteInFile(str + " " + time.ctime(time.time()), "out.txt")
    writingThread.start()
    print("The Main continues ... ")
    print("2^10 = ", 2**10)
    print("I'll wait until writing is completed.")
    writingThread.join()

if __name__ == "__main__":
    Main()
