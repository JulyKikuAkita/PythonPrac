__source__ = 'https://leetcode.com/problems/assign-cookies/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/assign-cookies.py
# Time:  O(nlogn)
# Space: O(1)
#
# Description: Leetcode # 455. Assign Cookies
#
# Assume you are an awesome parent and want to give your children some cookies.
# But, you should give each child at most one cookie. Each child i has a greed factor gi,
# which is the minimum size of a cookie that the child will be content with;
# and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i,
# and the child i will be content.
# Your goal is to maximize the number of your content children and output the maximum number.
#
# Note:
# You may assume the greed factor is always positive.
# You cannot assign more than one cookie to one child.
#
# Example 1:
# Input: [1,2,3], [1,1]
#
# Output: 1
#
# Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3.
# And even though you have 2 cookies, since their size is both 1,
# you could only make the child whose greed factor is 1 content.
# You need to output 1.
# Example 2:
# Input: [1,2], [1,2,3]
#
# Output: 2
#
# Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2.
# You have 3 cookies and their sizes are big enough to gratify all of the children,
# You need to output 2.
#
import unittest

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()

        result, i = 0, 0
        for j in xrange(len(s)):
            if i == len(g):
                break
            if s[j] >= g[i]:
                result += 1
                i += 1
        return result

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:

#15ms 41.1%
class Solution {
   public static int findContentChildren(int[] g, int[] s) {
    if(g == null || s == null){ return 0; }
        Arrays.sort(g);
        Arrays.sort(s);
        int i = 0;
        for (int j = 0; i < g.length && j < s.length; j++) {
            if (g[i] <= s[j]) {
                i++;
            }
        }
        return i;
    }
}

#10ms 99.66%
class Solution {
   public static int findContentChildren(int[] g, int[] s) {
    //if(g == null || s == null){ return 0; }
        Arrays.sort(g);
        Arrays.sort(s);
        int result = 0;
        int l = 0, r = 0;
        while(l < g.length && r < s.length){
        	if(s[r] >= g[l]){
        		++ result;
        		++ l;
        		++ r;
        	}else{
        		++ r;
        	}
        }
        return result;
    }
}

# TreeMap
# 30ms 8.67%
class Solution {
   public static int findContentChildren(int[] g, int[] s) {
    	int count = 0;
    	TreeMap<Integer,Integer> tree = new TreeMap<>();
    	for(int temp : s){
    		Integer num = tree.get(temp);
    		num = num==null?0:num;
    		tree.put(temp,num+1);
    	}
    	for(int temp : g){
    		Integer targ = tree.ceilingKey(temp);
    		if(targ!=null){
    			Integer num = tree.get(targ);
    			if(num>0){
    				count++;
    				if(num==1){
    					tree.remove(targ);
    				}else{
                                        tree.put(targ, num - 1);
                                }
    			}
    		}
    	}
        return count;
    }
}
'''