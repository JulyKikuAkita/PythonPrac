__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/longest-consecutive-sequence.py
# Time:  O(n)
# Space: O(n)
#
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
#
# Your algorithm should run in O(n) complexity.
#  Google Facebook
# Hide Tags Array Union Find
# Hide Similar Problems (M) Binary Tree Longest Consecutive Sequence

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

# java solution
# http://www.programcreek.com/2013/01/leetcode-longest-consecutive-sequence-java/

#test
test = Solution()
seq1 = [100, 4, 200, 1, 3, 2]
#print test.longestConsecutive(seq1)

if __name__ =="__main__":
    # print Solution().longestConsecutive([100, 4, 200, 1, 3, 2])
    print Solution().longestConsecutive([1, 4, 3,2,2,2,0 , -1])

#java
js = '''
public class Solution {
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
                }
                max = Math.max(max, y -x);
            }
        }
        return max;
    }
}
'''