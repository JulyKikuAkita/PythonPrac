__source__ = 'https://leetcode.com/problems/maximum-frequency-stack/'
# Time:  O(1)
# Space: O(N)
#
# Description: Leetcode # 895. Maximum Frequency Stack
#
# Implement FreqStack, a class which simulates the operation of a stack-like data structure.
#
# FreqStack has two functions:
#
#     push(int x), which pushes an integer x onto the stack.
#     pop(), which removes and returns the most frequent element in the stack.
#         If there is a tie for most frequent element,
#           the element closest to the top of the stack is removed and returned.
#
# Example 1:
#
# Input:
# ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
# [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
# Output: [null,null,null,null,null,null,null,5,7,5,4]
# Explanation:
# After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to top.  Then:
#
# pop() -> returns 5, as 5 is the most frequent.
# The stack becomes [5,7,5,7,4].
#
# pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the top.
# The stack becomes [5,7,5,4].
#
# pop() -> returns 5.
# The stack becomes [5,7,4].
#
# pop() -> returns 4.
# The stack becomes [5,7].
#
# Note:
#
#     Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
#     It is guaranteed that FreqStack.pop() won't be called if the stack has zero elements.
#     The total number of FreqStack.push calls will not exceed 10000 in a single test case.
#     The total number of FreqStack.pop calls will not exceed 10000 in a single test case.
#     The total number of FreqStack.push and FreqStack.pop calls will not exceed 150000 across all test cases.
#
import unittest
import collections
# 272ms 82.18%
class FreqStack(object):

    def __init__(self):
        self.freq = collections.Counter()
        self.group = collections.defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x)

    def pop(self):
        """
        :rtype: int
        """
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1
        return x

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/maximum-frequency-stack/solution/
#
Approach 1: Stack of Stacks
Complexity Analysis
Time Complexity: O(1) for both push and pop operations.
Space Complexity: O(N), where N is the number of elements in the FreqStack. 

# 180ms 31.88%
class FreqStack {
    Map<Integer, Integer> freq;
    Map<Integer, Stack<Integer>> group;
    int maxfreq;
    
    public FreqStack() {
        freq = new HashMap();
        group = new HashMap();
        maxfreq = 0;
    }
    
    public void push(int x) {
        int f = freq.getOrDefault(x, 0) + 1;
        freq.put(x, f);
        if (f > maxfreq)
            maxfreq = f;
        group.computeIfAbsent(f, z -> new Stack()).push(x);
    }
    
    public int pop() {
        int x = group.get(maxfreq).pop();
        freq.put(x, freq.get(x) - 1);
        if (group.get(maxfreq).size() == 0)
            maxfreq--;
        return x;
    }
}
/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = new FreqStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 */
 
# 104ms 100%
class FreqStack {
    Map<Integer, Integer> freqMap;
    List<List<Integer>> freqList;
    
    public FreqStack() {
        freqMap = new HashMap<>();
        freqList = new ArrayList<>();
    }
    
    public void push(int x) {
        freqMap.put(x, freqMap.getOrDefault(x, 0) + 1);
        List<Integer> list = null;
        int freq = freqMap.get(x);
        if (freqList.size() < freq) {
            list = new ArrayList();
            freqList.add(list);
        } else {
            list = freqList.get(freq - 1);
        }
        list.add(x);
    }
    
    public int pop() {
        int highest = freqList.size() - 1;
        List<Integer> list = freqList.get(highest);
        int result = list.remove(list.size() - 1);
        freqMap.put(result, freqMap.get(result) - 1);
        if (list.size() == 0) {
            freqList.remove(highest);
        }
        return result;
    }
}

'''
