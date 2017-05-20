__author__ = 'July'
import time
import urllib2
import threading

# Single threaded way:
class singleThread:

    def get_responses(self):
        urls = ['http://www.google.com', 'http://www.amazon.com', 'http://www.ebay.com', 'http://www.facebook.com', 'https://en.wikipedia.org/wiki/Main_Page']
        start = time.time()
        for url in urls:
            print url
            resp = urllib2.urlopen(url)
            print resp.getcode()
        print "Single Thread Elapsed time: %s" % (time.time()-start)

class GetUrlThread(threading.Thread):

    def __init__(self, url):
        self.url = url
        super(GetUrlThread, self).__init__()

    def run(self):
        resp = urllib2.urlopen(self.url)
        print self.url, resp.getcode()

"""
We don't want the elapsed time to be evaluated until all the threads have executed, join() comes in picture here.
Calling join() on a thread tells the main thread to wait for this particular thread to finish before the main thread can execute the next instruction.
We call join() on all the threads, so elapsed time will be printed only after all the threads have run.
Few things about threads
Processor might not execute run() of a thread immediately after start().
You can't say in which order run() of different threads will be called.
For a specific thread, it's guaranteed that the statements inside run() will be executed sequentially.
It means that first the the url associated with the thread will be fetched and only then the recieved response will be printed.
"""

if __name__ == "__main__":
    singleThread().get_responses()
    urls = ['http://www.google.com', 'http://www.amazon.com', 'http://www.ebay.com', 'http://www.facebook.com', 'https://en.wikipedia.org/wiki/Main_Page']

    start = time.time()
    threads = []

    for url in urls:
        t = GetUrlThread(url)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print "Multithread Elapsed time: %s" % (time.time()-start)
