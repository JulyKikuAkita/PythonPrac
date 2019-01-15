__source__ = 'https://leetcode.com/problems/design-hashmap/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 706. Design HashMap
#
# Design a HashMap without using any built-in hash table libraries.
#
# To be specific, your design should include these functions:
#
# put(key, value) : Insert a (key, value) pair into the HashMap.
# If the value already exists in the HashMap, update the value.
# get(key): Returns the value to which the specified key is mapped,
# or -1 if this map contains no mapping for the key.
# remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.
#
# Example:
#
# MyHashMap hashMap = new MyHashMap();
# hashMap.put(1, 1);
# hashMap.put(2, 2);
# hashMap.get(1);            // returns 1
# hashMap.get(3);            // returns -1 (not found)
# hashMap.put(2, 1);          // update the existing value
# hashMap.get(2);            // returns 1
# hashMap.remove(2);          // remove the mapping for 2
# hashMap.get(2);            // returns -1 (not found)
#
# Note:
#
# All keys and values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashMap library.
#
import unittest

class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        bucket, idx = self._index(key)
        array = self.buckets[bucket]
        if idx < 0 :
            array.append((key, value))
        else:
            array[idx] = (key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        bucket, idx = self._index(key)
        if idx < 0:
            return -1
        array = self.buckets[bucket]
        key, value = array[idx]
        return value


    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        bucket, idx = self._index(key)
        if idx < 0:
            return
        array = self.buckets[bucket]
        del array[idx]

    def _bucket(self, key):
        return key % self.size

    def _index(self, key):
        bucket = self._bucket(key)
        for i, (k,v) in enumerate(self.buckets[bucket]):
            if k == key:
                return bucket, i
        return bucket, -1



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 81ms 94.18%
class MyHashMap {
    private class ListNode {
        int key, val;
        ListNode next;

        ListNode(int key, int val) {
            this.key = key;
            this.val = val;
        }
    }

    private ListNode[] buckets;

    /** Initialize your data structure here. */
    public MyHashMap() {
        buckets = new ListNode[1001];
    }

    /** value will always be non-negative. */
    public void put(int key, int value) {
        int i = idx(key);
        if (buckets[i] == null) buckets[i] = new ListNode(-1, -1);
        ListNode prev = find(buckets[i], key);
        if (prev.next == null) prev.next = new ListNode(key, value);
        else prev.next.val = value;
    }

    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    public int get(int key) {
        int i = idx(key);
        if (buckets[i] == null) return -1;
        ListNode node = find(buckets[i], key);
        return node.next == null ? -1 : node.next.val;
    }

    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    public void remove(int key) {
        int i = idx(key);
        if (buckets[i] == null) return;
        ListNode prev = find(buckets[i], key);
        if (prev.next == null) return;
        prev.next = prev.next.next;
    }

    private int idx(int key) {
        return Integer.hashCode(key) % buckets.length;
    }

    private ListNode find(ListNode bucket, int key) {
        ListNode node = bucket, prev = null;
        while (node != null && node.key != key) {
            prev = node;
            node = node.next;
        }
        return prev;
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */
'''