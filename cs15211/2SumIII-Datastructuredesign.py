__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/two-sum-iii-data-structure-design.py
# Time:  O(n)
# Space: O(n)
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
# LinkedIn
# Hide Tags Hash Table Design
# Hide Similar Problems (E) Two Sum (E) Unique Word Abbreviation

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

#test
if __name__ == "__main__":
    sol = TwoSum()
    for i in (1,3,5):
        sol.add(i)
    for i in (4,7):
        print sol.find(i)

# java
# http://www.programcreek.com/2014/03/two-sum-iii-data-structure-design-java/
js = '''
public class TwoSum {
    private Map<Integer, Boolean> map = new HashMap<>();

    // Add the number to an internal data structure.
	public void add(int number) {
	    if (map.containsKey(number)) {
	        map.put(number, true);
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
'''

js2 = ''' 85.05%
import java.util.LinkedHashMap;

public class TwoSum {
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

js3 = '''  92.39%
import java.util.LinkedHashMap;

public class TwoSum {
    Map<Integer, Boolean> map;

    public TwoSum() {
        map = new LinkedHashMap<>();
    }

    // Add the number to an internal data structure.
	public void add(int number) {
	    if (map.containsKey(number)) {
	        map.put(number, true);
	    } else {
	        map.put(number, false);
	    }
	}

    // Find if there exists any pair of numbers which sum is equal to the value.
	public boolean find(int value) {
	    for (Map.Entry<Integer, Boolean> entry : map.entrySet()) {
	        int key = entry.getKey();
	        boolean val = entry.getValue();
	        if (map.containsKey(value - key) && (key << 1 != value || val)) {
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
