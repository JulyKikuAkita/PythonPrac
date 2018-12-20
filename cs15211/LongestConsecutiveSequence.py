__source__ = 'https://leetcode.com/problems/longest-consecutive-sequence/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/longest-consecutive-sequence.py
# Time:  O(n)
# Space: O(n)
#
# Description: Leetcode # 128. Longest Consecutive Sequence
#
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
#
# Your algorithm should run in O(n) complexity.
# Companies
# Google Facebook
# Related Topics
# Array Union Find
# Similar Questions
# Binary Tree Longest Consecutive Sequence
#
import unittest
class Solution:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        result, lengths = 1, {key: 0 for key in num}
        print lengths

        for i in num:
            if lengths[i] == 0:
                lengths[i] = 1
                left, right = lengths.get(i-1, 0), lengths.get(i+1, 0) # dict.get(key. default=NOne)
                length = 1 + left + right
                result, lengths[i - left], lengths[i + right] = max(result, length), length, length
        return result

class Solution2:
    # @param num, a list of integer
    # @return an integer
    def longestConsecutive(self, num):
        dict = {x:False for x in num} #False = not visited
        maxLen = -1
        for i in dict:
            if dict[i] == False:
                curr = i+1
                len1 = 0
                while curr in dict and dict[curr] == False:
                    len1 += 1
                    dict[curr] = True
                    curr += 1
                curr = i -1
                len2 = 0
                while curr in dict and dict[curr] == False:
                    len2 += 1
                    dict[curr] = True
                    curr -= 1
                maxLen = max(maxLen, 1+len1+len2)

        return maxLen

#test
class TestMethods(unittest.TestCase):
    def test_Local(self):
        test = Solution()
        seq1 = [100, 4, 200, 1, 3, 2]
        #print test.longestConsecutive(seq1)
        print Solution().longestConsecutive([1, 4, 3,2,2,2,0 , -1])

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/longest-consecutive-sequence/solution/

We will use HashMap. The key thing is to keep track of the sequence length and
store that in the boundary points of the sequence. For example, as a result,
for sequence {1, 2, 3, 4, 5}, map.get(1) and map.get(5) should both return 5.

Whenever a new element n is inserted into the map, do two things:

See if n - 1 and n + 1 exist in the map, and if so, it means there is an existing sequence next to n.
Variables left and right will be the length of those two sequences,
while 0 means there is no sequence and n will be the boundary point later.
Store (left + right + 1) as the associated value to key n into the map.
Use left and right to locate the other end of the sequences to the left and right of n respectively,
and replace the value with the new length.
Everything inside the for loop is O(1) so the total time is O(n). Please comment if you see something wrong. Thanks.
1)
# 3ms 96.24%
class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length <= 1) return nums.length;
        Arrays.sort(nums);
        int max = 1, len = 1;
        int min = nums[0];
        for (int i = 1; i < nums.length; i++) {
            if (nums[i] - min == 1) {
                len++;
                min = nums[i];
            } else if (nums[i] - min > 1) {
                len = 1;
                min = nums[i];
            }
            max = Math.max(max, len);
        }
        return max;
    }
}

2)
Using a set to collect all elements that hasn't been visited.
search element will be O(1) and eliminates visiting element again.

# 9ms 50.78%
class Solution {
    public int longestConsecutive(int[] nums) {
        if(nums == null || nums.length == 0) return 0;

        Set<Integer> set = new HashSet<Integer>();

        for(int num: nums) set.add(num);
        int max = 0;
        for(int x: nums) {
            if ( !set.contains(x - 1)) {
                int y = x + 1;
                while( set.contains(y)){
                    y++;
                }  //additional++ when exist while loop
                max = Math.max(max, y - x);
            }
        }
        return max;
    }
}
'''
