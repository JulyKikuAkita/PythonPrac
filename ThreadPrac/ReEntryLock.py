__source__ = 'http://www.bogotobogo.com/python/Multithread/python_multithreading_Thread_Local_Specific_Data.php'
Reading='''
http://www.jianshu.com/p/40d4c7aebd66

'''
# Description:
# Implement a paxos like thread manager(or raft)
#
# SNAKE concept:
# Scenario:case/interface
# Necessary:constrain/hypothesis
# Application:service/algorithm
# Kilobit:data
# Evolve:

Thought = '''

#Thought: how to implement 1 to many reEntryLock manager (support only one server for now,
and will extends to distributed env),
- how to support multiple locker management?
- how to support edge case from reEntry? ex:, client down without release lock (with timestamp and set timeout)
- how long can client hold a lock with timeout settings? if the job is not finished the client needs to return lock?
(need to support reEntry)
- how to preserve persistent ?
need to have transaction log to recover service state (from latest snapshot) if server/client is down


Synchronize(this){
    boolean[] islocked[n]; //naive
    Lock[] islocked[n];
}

public void timeoutReleaseLock() {
    for(Lock l : isLocked) {
        if (l.isLocked && l.timestamp > 5 mins) l.isLocked = false;
    }
}

class Lock{
    boolean isLocked; //isLocked acquired by ppl?
    int pid; //know who acquires lock
    Date timestamp;//currentTime //set time out to release all lock
}

public void lock() {
    for (Object a: arr) {
        if (a.getLock()) {
            a.toThingsRequiresLock
            isLocked[a] = true;
        }
    }
}

//to be implement
public boolean releaseLock(){}
public boolean renewLock(){}

'''