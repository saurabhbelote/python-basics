# threads

import _thread
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % ( threadName, time.ctime(time.time()) ))

# Create two threads as follows
try:
   _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
   _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
except:
   print ("Error: unable to start thread")

while 1:
   pass



# asyncio
# countasync.py

import asyncio

async def count():
    print("One")
    await asyncio.sleep(1)
    print("Two")

async def main():
    await asyncio.gather(count(), count(), count())

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")


# multiprocessing

from multiprocessing import Process
my_numbers = input()
def cube(x):
    for x in (my_numbers):
        print('%s cube is %s' % (x, x**3))
sau =[1,3,54,6,7,4]        
def evenno(x):
    for x in (sau):
        if x % 2 == 0:
            print('%s is an even number ' % (x))
    if __name__ == '__main__':
        my_numbers = [3, 4, 5, 6, 7, 8]
        my_process1 = Process(target=cube, args=('x',))
        my_process2 = Process(target=evenno, args=('x',))
        my_process1.start()
        my_process2.start()
        my_process1.join()
    my_process2.join()
print ("Done")