__source__ = 'https://leetcode.com/problems/design-hashset/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 705. Design HashSet
#
# Design a HashSet without using any built-in hash table libraries.
#
# To be specific, your design should include these functions:
#
# add(value): Insert a value into the HashSet.
# contains(value) : Return whether the value exists in the HashSet or not.
# remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.
#
# Example:
#
# MyHashSet hashSet = new MyHashSet();
# hashSet.add(1);
# hashSet.add(2);
# hashSet.contains(1);    // returns true
# hashSet.contains(3);    // returns false (not found)
# hashSet.add(2);
# hashSet.contains(2);    // returns true
# hashSet.remove(2);
# hashSet.contains(2);    // returns false (already removed)
#
# Note:
#
# All values will be in the range of [0, 1000000].
# The number of operations will be in the range of [1, 10000].
# Please do not use the built-in HashSet library.
#
import unittest

# 96ms 100%
class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = set()

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.hashset.add(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if key in self.hashset:
            self.hashset.remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        if key in self.hashset:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 71ms 98.81%
class MyHashSet {

    private int buckets = 1000;
    private int itemsPerBucket = 1001;
    private boolean[][] table;

    /** Initialize your data structure here. */
    public MyHashSet() {
        table = new boolean[buckets][];
    }

    private int hash(int key) {
        return key % buckets;
    }

    private int pos(int key) {
        return key / buckets;
    }

    public void add(int key) {
        int hashkey = hash(key);

        if (table[hashkey] == null) {
            table[hashkey] = new boolean[itemsPerBucket];
        }
        table[hashkey][pos(key)] = true;
    }

    public void remove(int key) {
        int hashkey = hash(key);

        if (table[hashkey] != null)
            table[hashkey][pos(key)] = false;
    }

    /** Returns true if this set did not already contain the specified element */
    public boolean contains(int key) {
        int hashkey = hash(key);
        return table[hashkey] != null && table[hashkey][pos(key)];
    }
}
'''