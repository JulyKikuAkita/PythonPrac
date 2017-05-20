__author__ = 'July'
# http://chriskiehl.com/article/parallelism-in-one-line/
# http://jeffknupp.com/blog/2013/06/30/pythons-hardest-problem-revisited/
# http://www.dabeaz.com/python/UnderstandingGIL.pdf
'''
The idea is simple: if a single instance of the Python interpreter is constrained by the GIL,
one can achieve gains in concurrent workloads by through multiple interpreter processes in place of multiple threads.
Helpfully, multiprocessing was written with the same interface as the threading package,
so code already using threads doesn't require a massive rewrite to make use of multiple processes.

The most visible difference between processes and threads is the amount of access to shared data they permit.
'''
import time
import urllib2

# use pickle to share var between processes
from multiprocessing import Pool        # multi-processing concurrency
from multiprocessing.dummy import Pool as ThreadPool  # multi-threading concurrency
# try which one faster

# If you leave it blank, it will default to the number of Cores in your machine.
pool = ThreadPool(4)  # Sets the pool size to 4

urls = [
  'http://www.python.org',
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
  'http://planet.python.org/',
  'https://wiki.python.org/moin/LocalUserGroups',
  'http://www.python.org/psf/',
  'http://docs.python.org/devguide/',
  'http://www.python.org/community/awards/'
  # etc..
  ]


# Make the Pool of workers
# If you leave it blank, it will default to the number of Cores in your machine.
pool = ThreadPool(1)  # Sets the pool size to 1

results = []
start = time.time()
for url in urls:
# Open the urls in their own threads
# and return the results
  result = urllib2.urlopen(url)
  results.append(result)
end = time.time()
print "Single Thread:  {:03.3f} seconds".format(end - start)

# # ------- VERSUS ------- #
start = time.time()
pool = ThreadPool(1)
results = pool.map(urllib2.urlopen, urls)
end = time.time()
print "1 pool:  {:03.3f} seconds".format(end - start)


# # ------- 4 Pool ------- #
start = time.time()
pool = ThreadPool(4)
results = pool.map(urllib2.urlopen, urls)
end = time.time()
print "4 pool:  {:03.3f} seconds".format(end - start)
# # ------- 8 Pool ------- #

start = time.time()
pool = ThreadPool(8)
results = pool.map(urllib2.urlopen, urls)
end = time.time()
print "8 pool: {:03.3f} seconds".format(end - start)

# # ------- 13 Pool ------- #

start = time.time()
pool = ThreadPool(13)
results = pool.map(urllib2.urlopen, urls)
end = time.time()
print "13 pool:  {:03.3f} seconds".format(end - start)

#close the pool and wait for the work to finish
pool.close()
pool.join()