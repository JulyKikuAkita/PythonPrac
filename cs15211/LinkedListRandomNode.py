__source__ = 'https://leetcode.com/problems/linked-list-random-node/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/linked-list-random-node.py
# Time:  O(n) Reservoir sampling
# Space: O(1)
#
# Description: 382. Linked List Random Node
#
# Given a singly linked list, return a random node's value from the linked list.
# Each node must have the same probability of being chosen.
#
# Follow up:
# What if the linked list is extremely large and its length is unknown to you?
# Could you solve this efficiently without using extra space?
#
# Example:
#
# // Init a singly linked list [1,2,3].
# ListNode head = new ListNode(1);
# head.next = new ListNode(2);
# head.next.next = new ListNode(3);
# Solution solution = new Solution(head);
#
# // getRandom() should return either 1, 2, or 3 randomly.
# Each element should have equal probability of returning.
# solution.getRandom();
#
# Companies
# Google
# Related Topics
# Reservoir Sampling
# Similar Questions
# Random Pick Index
#

import unittest
from random import randint
class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head. Note that the head is guanranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.__head = head


    # Proof of Reservoir Sampling:
    # https://discuss.leetcode.com/topic/53753/brief-explanation-for-reservoir-sampling
    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        reservoir = self.__head.val
        curr, n = self.__head.next, 1
        while curr:
            reservoir = curr.val if randint(1, n+1) == 1 else reservoir
            curr, n = curr.next, n+1
        return reservoir


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: http://blog.jobbole.com/42550

After I read this one: http://blog.jobbole.com/42550/,

When we read the first node head, if the stream ListNode stops here,
we can just return the head.val. The possibility is 1/1.

When we read the second node, we can decide if we replace the result r or not.
The possibility is 1/2. So we just generate a random number between 0 and 1, and check if it is equal to 1.
If it is 1, replace r as the value of the current node, otherwise we don't touch r,
so its value is still the value of head.

When we read the third node, now the result r is one of value in the head or second node.
We just decide if we replace the value of r as the value of current node(third node).
The possibility of replacing it is 1/3, namely the possibility of we don't touch r is 2/3.
So we just generate a random number between 0 ~ 2, and if the result is 2 we replace r.
We can continue to do like this until the end of stream ListNode.

using "Reservoir sampling" O(1) space, O(n) time complexity
/*
  S has items to sample, R will contain the result
*/
ReservoirSample(S[1..n], R[1..k])
  // fill the reservoir array
  for i = 1 to k
      R[i] := S[i]

  // replace elements with gradually decreasing probability
  for i = k+1 to n
    j := random(1, i)   // important: inclusive range
    if j <= k
        R[j] := S[i]


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    ListNode mHead;
    Random random;

    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    public Solution(ListNode head) {
        mHead = head;
        random = new Random();
    }

    /** Returns a random node's value. */
    public int getRandom() {
        ListNode c = mHead;
        int r = c.val;
        for(int i=1;c.next != null;i++){
            c = c.next;
            if(random.nextInt(i + 1) == i) r = c.val;
        }
        return r;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */

#100% 108ms
class Solution {

    ListNode myHead;
    int len = 0;
    Random r = new Random();

    /** @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node. */
    public Solution(ListNode head) {
        myHead = head;
        while(head != null) {
            head = head.next;
            len++;
        }
    }

    /** Returns a random node's value. */
    public int getRandom() {
        int i = r.nextInt(len);
        ListNode head = myHead;
        while(i > 0 && head != null) {
            i--;
            head = head.next;
        }
        return head.val;

    }
}

'''