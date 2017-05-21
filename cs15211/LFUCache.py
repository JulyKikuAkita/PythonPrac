__author__ = 'July'#
# 460. LFU Cache Add to List
# https://leetcode.com/problems/lfu-cache/#/description
# Design and implement a data structure for Least Frequently Used (LFU) cache.
# It should support the following operations: get and put.
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item.
# For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency),
# the least recently used key would be evicted.
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LFUCache cache = new LFUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.get(3);       // returns 3.
# cache.put(4, 4);    // evicts key 1.
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# Hide Company Tags Amazon Google
# Hide Tags Design
# Hide Similar Problems (H) LRU Cache
#
java = '''
Java O(1) Accept Solution Using HashMap, DoubleLinkedList and LinkedHashSet
Two HashMaps are used, one to store <key, value> pair, another store the <key, node>.
I use double linked list to keep the frequent of each key. In each double linked list node,
keys with the same count are saved using java built in LinkedHashSet. This can keep the order.
Every time, one key is referenced, first find the current node corresponding to the key,
If the following node exist and the frequent is larger by one, add key to the keys of the following node,
else create a new node and add it following the current node.
All operations are guaranteed to be O(1).

public class LFUCache {
    private Node head = null;
    private int cap = 0;
    private HashMap<Integer, Integer> valueHash = null;
    private HashMap<Integer, Node> nodeHash = null;

    public LFUCache(int capacity) {
        this.cap = capacity;
        valueHash = new HashMap<Integer, Integer>();
        nodeHash = new HashMap<Integer, Node>();
    }

    public int get(int key) {
        if (valueHash.containsKey(key)) {
            increaseCount(key);
            return valueHash.get(key);
        }
        return -1;
    }

    public void put(int key, int value) {
        if ( cap == 0 ) return;
        if (valueHash.containsKey(key)) {
            valueHash.put(key, value);
        } else {
            if (valueHash.size() < cap) {
                valueHash.put(key, value);
            } else {
                removeOld();
                valueHash.put(key, value);
            }
            addToHead(key);
        }
        increaseCount(key);
    }

    private void addToHead(int key) {
        if (head == null) {
            head = new Node(0);
            head.keys.add(key);
        } else if (head.count > 0) {
            Node node = new Node(0);
            node.keys.add(key);
            node.next = head;
            head.prev = node;
            head = node;
        } else {
            head.keys.add(key);
        }
        nodeHash.put(key, head);
    }

    private void increaseCount(int key) {
        Node node = nodeHash.get(key);
        node.keys.remove(key);

        if (node.next == null) {
            node.next = new Node(node.count+1);
            node.next.prev = node;
            node.next.keys.add(key);
        } else if (node.next.count == node.count+1) {
            node.next.keys.add(key);
        } else {
            Node tmp = new Node(node.count+1);
            tmp.keys.add(key);
            tmp.prev = node;
            tmp.next = node.next;
            node.next.prev = tmp;
            node.next = tmp;
        }

        nodeHash.put(key, node.next);
        if (node.keys.size() == 0) remove(node);
    }

    private void removeOld() {
        if (head == null) return;
        int old = 0;
        for (int n: head.keys) {
            old = n;
            break;
        }
        head.keys.remove(old);
        if (head.keys.size() == 0) remove(head);
        nodeHash.remove(old);
        valueHash.remove(old);
    }

    private void remove(Node node) {
        if (node.prev == null) {
            head = node.next;
        } else {
            node.prev.next = node.next;
        }
        if (node.next != null) {
            node.next.prev = node.prev;
        }
    }

    class Node {
        public int count = 0;
        public LinkedHashSet<Integer> keys = null;
        public Node prev = null, next = null;

        public Node(int count) {
            this.count = count;
            keys = new LinkedHashSet<Integer>();
            prev = next = null;
        }
    }
}

Java solutions of three different ways. PriorityQueue : O(capacity) TreeMap : O(log(capacity)) DoubleLinkedList : O(1)
The first one: PriorityQueue + HashMap set O(capacity) get O(capacity)
The second one: TreeMap + HashMap set O(log(capacity)) get O(log(capacity))
The third one: HashMap + HashMap + DoubleLinkedList set O(1) get O(1)

1. PriorityQueue + HashMap: set O(capacity) get O(capacity) w/ Pair compareTo
public class LFUCache {
    long mStamp;
    int mCapacity;
    int mNum;
    PriorityQueue<Pair> mMinHeap;
    HashMap<Integer, Pair> mHashMap;

    public LFUCache(int capacity) {
        mCapacity = capacity;
        mNum = 0;
        mMinHeap = new PriorityQueue<Pair>();
        mHashMap = new HashMap<Integer, Pair>();
        mStamp = 0;
    }

    public int get(int key) {
        if (mCapacity == 0) return -1;
        if (mHashMap.containsKey(key)){
            Pair old = mHashMap.get(key);
            mMinHeap.remove(old);
            Pair newNode = new Pair(key, old.mValue, old.mTimes + 1, mStamp++);
            mHashMap.put(key, newNode);
            mMinHeap.offer(newNode);
            return mHashMap.get(key).mValue;
        }else {
            return -1;
        }
    }

    public void put(int key, int value) {
        if (mCapacity == 0) return;
        if (mHashMap.containsKey(key)) {
            Pair old = mHashMap.get(key);
            mMinHeap.remove(old);

            Pair newNode = new Pair(key, value, old.mTimes + 1, mStamp++);
            mHashMap.put(key, newNode);
            mMinHeap.offer(newNode);
        }else if(mNum == mCapacity) {
            Pair old = mMinHeap.poll();
            mHashMap.remove(old.mKey);

            Pair newNode = new Pair(key, value, 1, mStamp++);
            mHashMap.put(key, newNode);
            mMinHeap.offer(newNode);
        }else {
            mNum++;
            Pair p = new Pair(key, value, 1, mStamp++);
            mHashMap.put(key, p);
            mMinHeap.offer(p);
        }
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
 class Pair implements Comparable<Pair> {
     long mStamp;
     int mKey;
     int mValue;
     int mTimes;

     public Pair (int key, int value, int times, long stamp) {
         mStamp = stamp;
         mKey = key;
         mValue = value;
         mTimes = times;
     }

     public int compareTo(Pair that) {
         if (mTimes == that.mTimes) {
             return (int) (mStamp - that.mStamp);
         } else {
             return mTimes - that.mTimes;
         }
     }
 }

 2. TreeMap + HashMap: set O(log(capacity)) get O(log(capacity))
public class LFUCache {
    private int mCapacity;
    private int mStamp;
    private HashMap<Integer, Tuple> mHashMap;
    private TreeMap<Tuple, Integer> mTreeMap;

    public LFUCache(int capacity) {
        mCapacity = capacity;
        mStamp = 0;
        mHashMap = new HashMap<Integer, Tuple>();
        mTreeMap = new TreeMap<Tuple, Integer>( new Comparator<Tuple>(){
            public int compare(Tuple t1, Tuple t2) {
                if (t1.mTimes == t2.mTimes) {
                    return t1.mStamp - t2.mStamp;
                }
                return t1.mTimes - t2.mTimes;
            }
        });
    }

    public int get(int key) {
        if (mCapacity == 0) {
            return -1;
        }

        if (!mHashMap.containsKey(key)){
            return -1;
        }

        Tuple old = mHashMap.get(key);
        mTreeMap.remove(old);
        Tuple t = new Tuple(old.mVal, mStamp++, old.mTimes + 1);

        mTreeMap.put(t, key);
        mHashMap.put(key, t);
        return old.mVal;
    }

    public void put(int key, int value) {
        if (mCapacity == 0) return;

        if (mHashMap.containsKey(key)){
            Tuple old = mHashMap.get(key);
            Tuple t = new Tuple(value, mStamp++, old.mTimes + 1);
            mTreeMap.remove(old);
            mHashMap.put(key, t);
            mTreeMap.put(t, key);
        } else {
            if (mTreeMap.size() == mCapacity) {
                int endKey = mTreeMap.pollFirstEntry().getValue();
                mHashMap.remove(endKey);
            }
            Tuple t = new Tuple(value, mStamp++, 1);
            mHashMap.put(key, t);
            mTreeMap.put(t, key);
        }
    }
    private class Tuple {
         int mVal;
         int mTimes;
         int mStamp;
         public Tuple (int val, int stamp, int times) {
             mVal = val;
             mTimes = times;
             mStamp = stamp;
         }
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */


 3. The third one: HashMap + HashMap + DoubleLinkedList set O(1) get O(1)

'''