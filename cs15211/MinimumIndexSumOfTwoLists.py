__source__ = 'https://leetcode.com/problems/minimum-index-sum-of-two-lists/'
# Time:  O( n + m)
# Space: O(n)
#
# Description: 599. Minimum Index Sum of Two Lists
#
# Suppose Andy and Doris want to choose a restaurant for dinner,
# and they both have a list of favorite restaurants represented by strings.
#
# You need to help them find out their common interest with the least list index sum.
# If there is a choice tie between answers, output all of them with no order requirement.
# You could assume there always exists an answer.
#
# Example 1:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
# Output: ["Shogun"]
# Explanation: The only restaurant they both like is "Shogun".

# Example 2:
# Input:
# ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# ["KFC", "Shogun", "Burger King"]
# Output: ["Shogun"]
# Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
#
# Note:
# The length of both lists will be in the range of [1, 1000].
# The length of strings in both lists will be in the range of [1, 30].
# The index is starting from 0 to the list length minus 1.
# No duplicates in both lists.
# Hide Company Tags Yelp
# Hide Tags Hash Table
# Hide Similar Problems (E) Intersection of Two Linked Lists
#
# Explanation:
# Say the lists are A and B. Let Aindex[element] be the index of that element in A.
# For every index, value pair (j, v) in B, we have some candidate sum-of-indexes i + j,
# where i = Aindex[v] if it exists.
# If the candidate sum is better, it becomes our new answer;
# if the candidate sums are the same, then we append to our answer.
#
import unittest

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        Aindex = {u: i for i, u in enumerate(list1)}
        best, ans = 1e9, []

        for j, v in enumerate(list2):
            i = Aindex.get(v, 1e9)
            if i + j < best:
                best = i + j
                ans = [v]
            elif i + j == best:
                ans.append(v)
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/minimum-index-sum-of-two-lists/solution/

# 13ms 98.50%
class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        Map<String, Integer> map = new HashMap<>();
        List<String> res = new LinkedList<>();
        int minSum = Integer.MAX_VALUE;
        for (int i=0;i<list1.length;i++) map.put(list1[i], i);
        for (int i=0;i<list2.length;i++) {
            Integer j = map.get(list2[i]);
            if ( j != null && i + j <= minSum) {
                if (i + j < minSum) { res = new LinkedList<>(); minSum = i+j; }
                res.add(list2[i]);
            }
        }
        return res.toArray(new String[res.size()]);
    }
}
'''
