__source__ = 'https://leetcode.com/problems/split-linked-list-in-parts/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 725. Split Linked List in Parts
#
# Given a (singly) linked list with head node root,
# write a function to split the linked list into k consecutive linked list "parts".
#
# The length of each part should be as equal as possible:
# no two parts should have a size differing by more than 1.
# This may lead to some parts being null.
#
# The parts should be in order of occurrence in the input list,
# and parts occurring earlier should always have a size greater than or equal parts occurring later.
#
# Return a List of ListNode's representing the linked list parts that are formed.
#
# Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
# Example 1:
# Input:
# root = [1, 2, 3], k = 5
# Output: [[1],[2],[3],[],[]]
# Explanation:
# The input and each element of the output are ListNodes, not arrays.
# For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3,
# and root.next.next.next = null.
# The first element output[0] has output[0].val = 1, output[0].next = null.
# The last element output[4] is null, but it's string representation as a ListNode is [].
# Example 2:
# Input:
# root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
# Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
# Explanation:
# The input has been split into consecutive parts with size difference at most 1,
# and earlier parts are a larger size than the later parts.
# Note:
#
# The length of root will be in the range [0, 1000].
# Each value of a node in the input will be an integer in the range [0, 999].
# k will be an integer in the range [1, 50].
#
import unittest

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#28ms 96.78%
class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        cur = root
        for N in xrange(1001):
            if not cur: break
            cur = cur.next
        width, remainder = divmod(N, k)

        ans = []
        cur = root
        for i in xrange(k):
            head = cur
            for j in xrange(width + (i < remainder) - 1):
                if cur: cur = cur.next
            if cur:
                cur.next, cur = None, cur.next
            ans.append(head)
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/split-linked-list-in-parts/solution/
#
Approach #1: Create New Lists [Accepted]
Complexity Analysis
Time Complexity: O(N + k), where N is the number of nodes in the given list.
If k is large, it could still require creating many new empty lists.
Space Complexity: O(max(N, k)), the space used in writing the answer.

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
# 2ms 100%
class Solution {
    public ListNode[] splitListToParts(ListNode root, int k) {
        ListNode cur = root;
        int N = 0;
        while (cur != null) {
            cur = cur.next;
            N++;
        }

        int width = N / k, rem = N % k;

        ListNode[] ans = new ListNode[k];
        cur = root;
        for (int i = 0; i < k; ++i) {
            ListNode head = new ListNode(0), write = head;
            for (int j = 0; j < width + (i < rem ? 1 : 0); ++j) {
                write = write.next = new ListNode(cur.val);
                if (cur != null) cur = cur.next;
            }
            ans[i] = head.next;
        }
        return ans;
    }
}

Approach #2: Split Input List [Accepted]
Complexity Analysis
Time Complexity: O(N + k), where N is the number of nodes in the given list.
If k is large, it could still require creating many new empty lists.
Space Complexity: O(k), the additional space used in writing the answer.

# 2ms 100%
class Solution {
    public ListNode[] splitListToParts(ListNode root, int k) {
        ListNode cur = root;
        int N = 0;
        while (cur != null) {
            cur = cur.next;
            N++;
        }

        int width = N / k, rem = N % k;

        ListNode[] ans = new ListNode[k];
        cur = root;
        for (int i = 0; i < k; ++i) {
            ListNode head = cur;
            for (int j = 0; j < width + (i < rem ? 1 : 0) - 1; ++j) {
                if (cur != null) cur = cur.next;
            }
            if (cur != null) {
                ListNode prev = cur;
                cur = cur.next;
                prev.next = null;
            }
            ans[i] = head;
        }
        return ans;
    }
}
'''
