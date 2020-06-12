from threading import Thread
def fun():
    for i in range(100000000):
        pass
    print("Fun")
def bun():
    for i in range(100):
        pass
    print("Bun")

thread1=Thread(target=fun)
thread1.start()
bun()
