__source__ = 'https://leetcode.com/problems/two-sum-iii-data-structure-design/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/two-sum-iii-data-structure-design.py
# Time:  O(n)
# Space: O(n)
#
# Description: Leetcode # 170. Two Sum III - Data structure design
#
# Design and implement a TwoSum class. It should support the following operations: add and find.
#
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.
#
# For example,
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false
#
# Companies
# LinkedIn
# Related Topics
# Hash Table Design
# Similar Questions
# Two Sum Unique Word Abbreviation Two Sum IV - Input is a BST
#
import unittest
class TwoSum:

    # initialize your data structure here
    def __init__(self):
        self.lookup = {}


    # @return nothing
    def add(self, number):
        if number in self.lookup:
            self.lookup[number] += 1
        else:
            self.lookup[number] = 1

    # @param value, an integer
    # @return a Boolean
    def find(self, value):
        for key in self.lookup:
            num = value - key
            if num in self.lookup and (num != key or self.lookup[key] > 1):
                return True
        return False

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)
        sol = TwoSum()
        for i in (1,3,5):
            sol.add(i)
        for i in (4,7):
            print sol.find(i)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought:
# Map with count

# 163ms 54.80%
class TwoSum {
    private HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();

    public void add(int number) {
        map.put(number, map.containsKey(number) ? map.get(number) + 1 : 1);
    }

    public boolean find(int value) {
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            int i = entry.getKey();
            int j = value - i;
            if ((i == j && entry.getValue() > 1) || (i != j && map.containsKey(j))) {
                return true;
            }
        }
        return false;
    }
}

# 128ms 91.32%
class TwoSum {
    private List<Integer> list = new ArrayList<Integer>();
    private Map<Integer, Integer> map = new HashMap<Integer, Integer>();

    // Add the number to an internal data structure.
	public void add(int number) {
	    if (map.containsKey(number)) map.put(number, map.get(number) + 1);
	    else {
	        map.put(number, 1);
	        list.add(number);
	    }
	}

    // Find if there exists any pair of numbers which sum is equal to the value.
	public boolean find(int value) {
	    for (int i = 0; i < list.size(); i++){
	        int num1 = list.get(i), num2 = value - num1;
	        if ((num1 == num2 && map.get(num1) > 1) || (num1 != num2 && map.containsKey(num2))) return true;
	    }
	    return false;
	}
}


# Map with Int
# 151ms 76.94%
class TwoSum {
    private Map<Integer, Boolean> map = new HashMap<>();

    // Add the number to an internal data structure.
	public void add(int number) {
	    if (map.containsKey(number)) {
	        map.put(number, true); //has dup
	    } else {
	        map.put(number, false);
	    }
	}

    // Find if there exists any pair of numbers which sum is equal to the value.
	public boolean find(int value) {
	    for(Integer key : map.keySet()) {
	        if (map.containsKey(value - key) && (value - key != key || map.get(key))) {
	            return true;
	        }
	    }
	    return false;
	}
}

# LinkedHashmap with Long
# 200ms 25.31%

import java.util.LinkedHashMap;
class TwoSum {
    Map<Long, Boolean> numDuplicateMap;

    public TwoSum() {
        numDuplicateMap = new LinkedHashMap<>();
    }

    // Add the number to an internal data structure.
	public void add(int number) {
	    long num = (long) number;
	    numDuplicateMap.put(num, numDuplicateMap.containsKey(num) ? true : false);
	}

    // Find if there exists any pair of numbers which sum is equal to the value.
	public boolean find(int value) {
	    for (Map.Entry<Long, Boolean> entry : numDuplicateMap.entrySet()) {
	        long key = entry.getKey();
	        boolean val = entry.getValue();
	        if (numDuplicateMap.containsKey((long) value - key) && (value >> 1 != key || val)) {
	            return true;
	        }
	    }
	    return false;
	}
}


// Your TwoSum object will be instantiated and called as such:
// TwoSum twoSum = new TwoSum();
// twoSum.add(number);
// twoSum.find(value);
'''
