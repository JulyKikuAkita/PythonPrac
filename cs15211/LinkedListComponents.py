__source__ = 'https://leetcode.com/problems/linked-list-components/'
# Time:  O(N + G.length), where N is the length of the linked list with root node head.
# Space: O(G.length)
#
# Description: Leetcode # 817. Linked List Components
#
# We are given head, the head node of a linked list containing unique integer values.
#
# We are also given the list G, a subset of the values in the linked list.
#
# Return the number of connected components in G,
# where two values are connected if they appear consecutively in the linked list.
#
# Example 1:
#
# Input:
# head: 0->1->2->3
# G = [0, 1, 3]
# Output: 2
# Explanation:
# 0 and 1 are connected, so [0, 1] and [3] are the two connected components.
# Example 2:
#
# Input:
# head: 0->1->2->3->4
# G = [0, 3, 1, 4]
# Output: 2
# Explanation:
# 0 and 1 are connected, 3 and 4 are connected, so [0, 1] and [3, 4] are the two connected components.
# Note:
#
# If N is the length of the linked list given by head, 1 <= N <= 10000.
# The value of each node in the linked list will be in the range [0, N - 1].
# 1 <= G.length <= 10000.
# G is a subset of all values in the linked list.
#
import unittest

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 80ms 90.46%
class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        Gset = set(G)
        cur = head
        ans = 0
        while cur:
            if (cur.val in Gset and
                    getattr(cur.next, 'val', None) not in Gset):
                ans += 1
            cur = cur.next
        return ans

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/linked-list-components/solution/
#
Approach #1: Grouping [Accepted]
Complexity Analysis
Time Complexity: O(N+G.length), where N is the length of the linked list with root node head.
Space Complexity: O(G.length), to store Gset.

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

# 17ms 45.77%
class Solution {
    public int numComponents(ListNode head, int[] G) {
        Set<Integer> Gset = new HashSet();
        for (int x: G) Gset.add(x);

        ListNode cur = head;
        int ans = 0;

        while (cur != null) {
            if (Gset.contains(cur.val) &&
                    (cur.next == null || !Gset.contains(cur.next.val)))
                ans++;
            cur = cur.next;
        }

        return ans;
    }
}

# 3ms 100%
class Solution {
    public int numComponents(ListNode head, int[] G) {
        int count = 0;
        ListNode tmp = head;
        while (tmp != null) {
            tmp = tmp.next;
            count++;
        }
        
        boolean[] present= new boolean[count];
        for (int g : G) {
            present[g] = true;
        }
        
        int res = 0;
        while (head != null) {
            if (present[head.val]) {
                res++;
                while (head != null && present[head.val]) head = head.next;
            } else {
                head = head.next;
            }
        }
        return res;
    }
}
'''
