__author__ = " http://agiliq.com/blog/2013/10/producer-consumer-problem-in-python/ "
# Demo a buggy example
from threading import Thread, Lock
import time
import random

queue = []
lock = Lock()

class ProducerThread(Thread):
    def run(self):
        nums = range(5) #Will create the list [0, 1, 2, 3, 4]
        global queue
        while True:
            num = random.choice(nums) #Selects a random number from list [0, 1, 2, 3, 4]
            lock.acquire()
            queue.append(num)
            print "Produced", num
            lock.release()
            time.sleep(random.random())


class ConsumerThread(Thread):
    def run(self):
        global queue
        while True:
            lock.acquire()
            if not queue:
                print "Nothing in queue, but consumer will try to consume"
            num = queue.pop(0)
            print "Consumed", num
            lock.release()
            time.sleep(random.random())


#ProducerThread().start()
#ConsumerThread().start()

"""
Explanation:
We started one producer thread(hereafter referred as producer) and one consumer thread(hereafter referred as consumer).
Producer keeps on adding to the queue and consumer keeps on removing from the queue.
Since queue is a shared variable, we keep it inside lock to avoid race condition.
At some point, consumer has consumed everything and producer is still sleeping. Consumer tries to consume more but since queue is empty, an IndexError is raised.
But on every execution, before IndexError is raised you will see the print statement telling "Nothing in queue,
but consumer will try to consume", which explains why you are getting the error.
We found this implementaion as the wrong behaviour.

What is the correct behaviour?
When there was nothing in the queue, consumer should have stopped running and waited instead of trying to consume from the queue.
And once producer adds something to the queue, there should be a way for it to notify the consumer telling it has added something to queue.
So, consumer can again consume from the queue. And thus IndexError will never be raised.
"""

class ProducerThread2(Thread):
    def run(self):
        nums = range(5) #Will create the list [0, 1, 2, 3, 4]
        global queue
        while True:
            num = random.choice(nums) #Selects a random number from list [0, 1, 2, 3, 4]
            with lock:
                queue.append(num)
                print "Produced", num, len(queue)
                print "Lock acquired via with"
            time.sleep(random.random())


class ConsumerThread2(Thread):
    def run(self):
        global queue
        while True:
            lock.acquire()
            if not queue:
                print "Nothing in queue, but consumer will try to consume"
            try:
                num = queue.pop(0)
                print "Consumed", num
            finally:
                lock.release()
            #time.sleep(random.random())


ProducerThread2().start()
ConsumerThread2().start()
ConsumerThread2().start()