__source__ = 'https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/insert-delete-getrandom-o1-duplicates-allowed.py
# Time:  O(1)
# Space: O(n)
#
# Description: Leetcode # 381. Insert Delete GetRandom O(1) - Duplicates allowed
#
# Design a data structure that supports all following operations in average O(1) time.
#
# Note: Duplicate elements are allowed.
# insert(val): Inserts an item val to the collection.
# remove(val): Removes an item val from the collection if present.
# getRandom: Returns a random element from current collection of elements.
# The probability of each element being returned is linearly related to
# the number of same value the collection contains.
# Example:
#
# // Init an empty collection.
# RandomizedCollection collection = new RandomizedCollection();
#
# // Inserts 1 to the collection. Returns true as the collection did not contain 1.
# collection.insert(1);
#
# // Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
# collection.insert(1);
#
# // Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
# collection.insert(2);
#
# // getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
# collection.getRandom();
#
# // Removes 1 from the collection, returns true. Collection now contains [1,2].
# collection.remove(1);
#
# // getRandom should return 1 and 2 both equally likely.
# collection.getRandom();
#
#
# Companies
# Yelp
# Related Topics
# Array Hash Table Design
# Similar Questions
# Insert Delete GetRandom O(1)
#
from random import randint, choice
from collections import defaultdict
import unittest

def __init__(self):
        self.vals, self.idxs = [], defaultdict(set)
# 80ms 100%
class RandomizedCollection(object):

    def insert(self, val):
        self.vals.append(val)
        self.idxs[val].add(len(self.vals) - 1)
        return len(self.idxs[val]) == 1


    def remove(self, val):
        if self.idxs[val]:
            out, ins = self.idxs[val].pop(), self.vals[-1]
            self.vals[out] = ins
            if self.idxs[ins]:
                self.idxs[ins].add(out)
                self.idxs[ins].discard(len(self.vals) - 1)
            self.vals.pop()
            return True
        return False

    def getRandom(self):
        return choice(self.vals)


# #
# FailedTC =
# ["RandomizedCollection","insert","insert","insert","insert","insert","remove","remove","remove","insert","remove","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom"]
# [[],[1],[1],[2],[2],[2],[1],[1],[2],[1],[2],[],[],[],[],[],[],[],[],[],[]]
# #

class RandomizedCollectionNOTAccept(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__list = []
        self.__used = defaultdict(list)


    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        has = val in self.__used

        self.__list += val,
        self.__used[val] += len(self.__list)-1,

        return not has


    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.__used:
            return False

        self.__used[self.__list[-1]][-1] = self.__used[val][-1]
        self.__list[self.__used[val][-1]], self.__list[-1] = self.__list[-1], self.__list[self.__used[val][-1]]

        self.__used[val].pop()
        if not self.__used[val]:
            self.__used.pop(val)
        self.__list.pop()

        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.__list[randint(0, len(self.__list)-1)]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:

# 114ms 12.34%
class RandomizedCollection {

    ArrayList<Integer> result;
    HashMap<Integer, LinkedHashSet<Integer>> map;

    public RandomizedCollection() {
        result = new ArrayList<Integer>();
        map = new HashMap<Integer, LinkedHashSet<Integer>>();
    }

    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    public boolean insert(int val) {
        // Add item to map if it doesn't already exist.
        boolean alreadyExists = map.containsKey(val);
        if(!alreadyExists) {
            map.put(val, new LinkedHashSet<Integer>());
        }
        map.get(val).add(result.size());
        result.add(val);
        return !alreadyExists;
    }

    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    public boolean remove(int val) {
        if(!map.containsKey(val)) {
            return false;
        }
        // Get arbitary index of the ArrayList that contains val
        LinkedHashSet<Integer> valSet = map.get(val);
        int indexToReplace = valSet.iterator().next();

        // Obtain the set of the number in the last place of the ArrayList
        int numAtLastPlace = result.get(result.size() - 1);
        LinkedHashSet<Integer> replaceWith = map.get(numAtLastPlace);

        // Replace val at arbitary index with very last number
        result.set(indexToReplace, numAtLastPlace);

        // Remove appropriate index
        valSet.remove(indexToReplace);

        // Don't change set if we were replacing the removed item with the same number
        if(indexToReplace != result.size() - 1) {
            replaceWith.remove(result.size() - 1);
            replaceWith.add(indexToReplace);
        }
        result.remove(result.size() - 1);

        // Remove map entry if set is now empty, then return
        if(valSet.isEmpty()) {
            map.remove(val);
        }
        return true;
    }

    /** Get a random element from the collection. */
    public int getRandom() {
        // Get linearly random item
        return result.get((int)(Math.random() * result.size()));
    }
}

# 84ms 42.51%
class RandomizedCollection {
    ArrayList<Integer> nums;
	HashMap<Integer, Set<Integer>> locs;
	java.util.Random rand = new java.util.Random();
    /** Initialize your data structure here. */
    public RandomizedCollection() {
        nums = new ArrayList<Integer>();
	    locs = new HashMap<Integer, Set<Integer>>();
    }

    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    public boolean insert(int val) {
        boolean contain = locs.containsKey(val);
	    if ( ! contain ) locs.put( val, new LinkedHashSet<Integer>() );
	    locs.get(val).add(nums.size());
	    nums.add(val);
	    return ! contain ;
    }

    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    public boolean remove(int val) {
        boolean contain = locs.containsKey(val);
	    if ( ! contain ) return false;
	    int loc = locs.get(val).iterator().next();
	    locs.get(val).remove(loc);
	    if (loc < nums.size() - 1 ) {
	       int lastone = nums.get( nums.size()-1 );
	       nums.set( loc , lastone );
	       locs.get(lastone).remove( nums.size()-1);
	       locs.get(lastone).add(loc);
	    }
	    nums.remove(nums.size() - 1);

	    if (locs.get(val).isEmpty()) locs.remove(val);
	    return true;
    }

    /** Get a random element from the collection. */
    public int getRandom() {
        return nums.get( rand.nextInt(nums.size()) );
    }
}

# 79ms 61.85%
class RandomizedCollection {
    ArrayList<Integer> nums;
	HashMap<Integer, Set<Integer>> locs;
	java.util.Random rand = new java.util.Random();
    /** Initialize your data structure here. */
    public RandomizedCollection() {
        nums = new ArrayList<Integer>();
	    locs = new HashMap<Integer, Set<Integer>>();
    }

    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    public boolean insert(int val) {
        boolean contain = locs.containsKey(val);
	    if ( ! contain ) locs.put( val, new LinkedHashSet<Integer>() );
	    locs.get(val).add(nums.size());
	    nums.add(val);
	    return ! contain ;
    }

    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    public boolean remove(int val) {
        boolean contain = locs.containsKey(val);
	    if ( ! contain ) return false;
	    int loc = locs.get(val).iterator().next();
	    locs.get(val).remove(loc);
	    if (loc < nums.size() - 1 ) {
	       int lastone = nums.get( nums.size()-1 );
	       nums.set( loc , lastone );
	       locs.get(lastone).remove( nums.size()-1);
	       locs.get(lastone).add(loc);
	    }
	    nums.remove(nums.size() - 1);

	    if (locs.get(val).isEmpty()) locs.remove(val);
	    return true;
    }

    /** Get a random element from the collection. */
    public int getRandom() {
        return nums.get( rand.nextInt(nums.size()) );
    }
}
'''