__source__ = 'https://leetcode.com/problems/all-oone-data-structure/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/all-oone-data-structure.py
# Time:  O()
# Space: O()
#
# Description: 432. All O`one Data Structure
#
# Implement a data structure supporting the following operations:
#
# Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1.
# Key is guaranteed to be a non-empty string.
# Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise decrements an existing key by 1.
# If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.
# GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".
# GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".
# Challenge: Perform all these in O(1) time complexity.
#
# Hide Company Tags Uber
# Hide Tags Design
#
import unittest

class Node(object):
    """
    double linked list node
    """
    def __init__(self, value, keys):
        self.value = value
        self.keys = keys
        self.prev = None
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head, self.tail = Node(0, set()), Node(0, set())
        self.head.next, self.tail.prev = self.tail, self.head

    def insert(self, pos, node):
        node.prev, node.next = pos.prev, pos
        pos.prev.next, pos.prev = node, node
        return node

    def erase(self, node):
        node.prev.next, node.next.prev = node.next, node.prev
        del node

    def empty(self):
        return self.head.next is self.tail

    def begin(self):
        return self.head.next

    def end(self):
        return self.tail

    def front(self):
        return self.head.next

    def back(self):
        return self.tail.prev


class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.bucket_of_key = {}
        self.buckets = LinkedList()

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key not in self.bucket_of_key:
            self.bucket_of_key[key] = self.buckets.insert(self.buckets.begin(), Node(0, set([key])))

        bucket, next_bucket = self.bucket_of_key[key], self.bucket_of_key[key].next
        if next_bucket is self.buckets.end() or next_bucket.value > bucket.value+1:
            next_bucket = self.buckets.insert(next_bucket, Node(bucket.value+1, set()))
        next_bucket.keys.add(key)
        self.bucket_of_key[key] = next_bucket

        bucket.keys.remove(key)
        if not bucket.keys:
            self.buckets.erase(bucket)

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key not in self.bucket_of_key:
            return

        bucket, prev_bucket = self.bucket_of_key[key], self.bucket_of_key[key].prev
        self.bucket_of_key.pop(key, None)
        if bucket.value > 1:
            if bucket is self.buckets.begin() or prev_bucket.value < bucket.value-1:
                prev_bucket = self.buckets.insert(bucket, Node(bucket.value-1, set()))
            prev_bucket.keys.add(key)
            self.bucket_of_key[key] = prev_bucket

        bucket.keys.remove(key)
        if not bucket.keys:
            self.buckets.erase(bucket)

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.buckets.empty():
            return ""
        return iter(self.buckets.back().keys).next()

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.buckets.empty():
            return ""
        return iter(self.buckets.front().keys).next()


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
Main idea is to maintain a list of Bucket's,
each Bucket contains all keys with the same count.

head and tail can ensure both getMaxKey() and getMaxKey() be done in O(1).
keyCountMap maintains the count of keys, countBucketMap provides O(1) access to a specific Bucket with given count.
Deleting and adding a Bucket in the Bucket list cost O(1), so both inc() and dec() take strict O(1) time.
#113ms 20.85%
public class AllOne {
    // maintain a doubly linked list of Buckets
    private Bucket head;
    private Bucket tail;
    // for accessing a specific Bucket among the Bucket list in O(1) time
    private Map<Integer, Bucket> countBucketMap;
    // keep track of count of keys
    private Map<String, Integer> keyCountMap;

    // each Bucket contains all the keys with the same count
    private class Bucket {
        int count;
        Set<String> keySet;
        Bucket next;
        Bucket pre;
        public Bucket(int cnt) {
            count = cnt;
            keySet = new HashSet<>();
        }
    }

    /** Initialize your data structure here. */
    public AllOne() {
        head = new Bucket(Integer.MIN_VALUE);
        tail = new Bucket(Integer.MAX_VALUE);
        head.next = tail;
        tail.pre = head;
        countBucketMap = new HashMap<>();
        keyCountMap = new HashMap<>();
    }

    /** Inserts a new key <Key> with value 1. Or increments an existing key by 1. */
    public void inc(String key) {
        if (keyCountMap.containsKey(key)) {
            changeKey(key, 1);
        } else {
            keyCountMap.put(key, 1);
            if (head.next.count != 1)
                addBucketAfter(new Bucket(1), head);
            head.next.keySet.add(key);
            countBucketMap.put(1, head.next);
        }
    }

    /** Decrements an existing key by 1. If Key's value is 1, remove it from the data structure. */
    public void dec(String key) {
        if (keyCountMap.containsKey(key)) {
            int count = keyCountMap.get(key);
            if (count == 1) {
                keyCountMap.remove(key);
                removeKeyFromBucket(countBucketMap.get(count), key);
            } else {
                changeKey(key, -1);
            }
        }
    }

    /** Returns one of the keys with maximal value. */
    public String getMaxKey() {
        return tail.pre == head ? "" : (String) tail.pre.keySet.iterator().next();
    }

    /** Returns one of the keys with Minimal value. */
    public String getMinKey() {
        return head.next == tail ? "" : (String) head.next.keySet.iterator().next();
    }

    // helper function to make change on given key according to offset
    private void changeKey(String key, int offset) {
        int count = keyCountMap.get(key);
        keyCountMap.put(key, count + offset);
        Bucket curBucket = countBucketMap.get(count);
        Bucket newBucket;
        if (countBucketMap.containsKey(count + offset)) {
            // target Bucket already exists
            newBucket = countBucketMap.get(count + offset);
        } else {
            // add new Bucket
            newBucket = new Bucket(count + offset);
            countBucketMap.put(count + offset, newBucket);
            addBucketAfter(newBucket, offset == 1 ? curBucket : curBucket.pre);
        }
        newBucket.keySet.add(key);
        removeKeyFromBucket(curBucket, key);
    }

    private void removeKeyFromBucket(Bucket bucket, String key) {
        bucket.keySet.remove(key);
        if (bucket.keySet.size() == 0) {
            removeBucketFromList(bucket);
            countBucketMap.remove(bucket.count);
        }
    }

    private void removeBucketFromList(Bucket bucket) {
        bucket.pre.next = bucket.next;
        bucket.next.pre = bucket.pre;
        bucket.next = null;
        bucket.pre = null;
    }

    // add newBucket after preBucket
    private void addBucketAfter(Bucket newBucket, Bucket preBucket) {
        newBucket.pre = preBucket;
        newBucket.next = preBucket.next;
        preBucket.next.pre = newBucket;
        preBucket.next = newBucket;
    }
}
'''