__author__ = 'July'
import threading
import time
import logging

FORMAT = '[%(levelname)s %(asctime)-8s]  (%(threadName)-30s)  %(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT, )
#more about logging https://docs.python.org/2/library/logging.html

def f(id):
    logging.debug('Starting')
    time.sleep(1)
    logging.debug('Exiting')


def f2():
    logging.debug('Starting')
    time.sleep(2)
    logging.debug('Exiting')


def deamonThread():
    logging.debug('Starting')
    time.sleep(5)
    logging.debug('Exiting')


class MyThread(threading.Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs=None, verbose=None):
        """
        To pass arguments to a custom thread type,
        we need to overload constructor to save the values in
        an instance attribute that can be seen in the subclass
        """
        super(MyThread, self).__init__(group=group, target=target, name=name, verbose=verbose)
        self.args = args
        self.kwargs = kwargs
        return

    def run(self):
        logging.debug('running with %s and %s', self.args, self.kwargs)
        return


if __name__ == "__main__":
    t1 = threading.Thread(name='non_deamon t1', target=f, args=('f',))
    t2 = threading.Thread(name='non_deamon_t2', target=f2, args=())

    d1 = threading.Thread(name='daemon1', target=deamonThread)
    d1.setDaemon(True)  #expecting no EXIT message for daemon thread as mainthread leaves without waiting daemon

    d2 = threading.Thread(name='daemon2', target=deamonThread)
    d2.setDaemon(True)

    t1.start()
    t2.start()
    d1.start()
    d2.start()
    d2.join(7.0)  #set to 3.0, mainthread left before it awake thus should se d2.isAlive() = True
    print "d2.isAlive()", d2.isAlive()
    t1.join()

