__source__ = 'https://leetcode.com/problems/design-phone-directory/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/design-phone-directory.py
# init:     Time: O(n), Space: O(n)
# get:      Time: O(1), Space: O(1)
# check:    Time: O(1), Space: O(1)
# release:  Time: O(1), Space: O(1)
#
# Description: Leetcode # 379. Design Phone Directory
#
# Design a Phone Directory which supports the following operations:
#
# get: Provide a number which is not assigned to anyone.
# check: Check if a number is available or not.
# release: Recycle or release a number.
# Example:
#
# // Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
# PhoneDirectory directory = new PhoneDirectory(3);
#
# // It can return any available phone number. Here we assume it returns 0.
# directory.get();
#
# // Assume it returns 1.
# directory.get();
#
# // The number 2 is available, so return true.
# directory.check(2);
#
# // It returns 2, the only number that is left.
# directory.get();
#
# // The number 2 is no longer available, so return false.
# directory.check(2);
#
# // Release number 2 back to the pool.
# directory.release(2);
#
# // Number 2 is available again, return true.
# directory.check(2);
#
# Companies
# Google
# Related Topics
# Linked List Design
#
import unittest
class PhoneDirectory2(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.available = set(range(maxNumbers))

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        return self.available.pop() if self.available else -1

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return number in self.available

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        self.available.add(number)

class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.__curr = 0
        self.__numbers = range(maxNumbers)
        self.__used = [False] * maxNumbers


    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if self.__curr == len(self.__numbers):
            return -1
        number = self.__numbers[self.__curr]
        self.__curr += 1
        self.__used[number] = True
        return number


    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        return 0 <= number < len(self.__numbers) and \
               not self.__used[number]


    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: void
        """
        if not 0 <= number < len(self.__numbers) or \
           not self.__used[number]:
            return
        self.__used[number] = False
        self.__curr -= 1
        self.__numbers[self.__curr] = number


# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
#65.42% 530ms
public class PhoneDirectory {
    Set<Integer> mUsed;
    Queue<Integer> mAvailable;
    int mMax;
    /** Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory. */
    public PhoneDirectory(int maxNumbers) {
         mUsed = new HashSet<Integer>();
         mAvailable = new LinkedList<Integer>();
         mMax = maxNumbers;
         for (int i = 0; i < mMax; i++) {
             mAvailable.offer(i);
         }
    }

    /** Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available. */
    public int get() {
        Integer res = mAvailable.poll();
        if (res == null) return -1;
        mUsed.add(res);
        return res;
    }

    /** Check if a number is available or not. */
    public boolean check(int number) {
        if (number >= mMax || number < 0) return false;
        return !mUsed.contains(number);
    }

    /** Recycle or release a number. */
    public void release(int number) {
        if (mUsed.remove(number)) {
            mAvailable.offer(number);
        }
    }
}

/**
 * Your PhoneDirectory object will be instantiated and called as such:
 * PhoneDirectory obj = new PhoneDirectory(maxNumbers);
 * int param_1 = obj.get();
 * boolean param_2 = obj.check(number);
 * obj.release(number);
 */

 #Binary set
 #98.43% 350ms
 class PhoneDirectory {
    private int mMax;
    private BitSet mUsed;
    private int mMinAvailable = -1;

    /** Initialize your data structure here
     @param maxNumbers - The maximum numbers that can be stored in the phone directory. */
    public PhoneDirectory(int maxNumbers) {
        mMax = maxNumbers;
        mUsed = new BitSet(maxNumbers);
        mMinAvailable = 0;
    }

    /** Provide a number which is not assigned to anyone.
     @return - Return an available number. Return -1 if none is available. */
    public int get() {
        if (mMinAvailable == mMax) return -1;
        int n = mMinAvailable;
        mUsed.set(mMinAvailable);
        mMinAvailable = mUsed.nextClearBit(mMinAvailable);
        return n;
    }

    /** Check if a number is available or not. */
    public boolean check(int number) {
        if (number < 0 || number >= mMax) return false;
        return !mUsed.get(number);
    }

    /** Recycle or release a number. */
    public void release(int number) {
        if (mUsed.get(number)) mUsed.clear(number);
        if (number < mMinAvailable) mMinAvailable = number;
    }
}
'''