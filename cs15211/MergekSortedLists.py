__source__ = 'https://leetcode.com/problems/merge-k-sorted-lists/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/merge-k-sorted-lists.py
# Time:  O(nlogk)
# Space: O(1)
# heap
#  LinkedIn Google Uber Airbnb Facebook Twitter Amazon Microsoft
# Hide Tags Divide and Conquer Linked List Heap
# Hide Similar Problems
#
# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
import heapq
# python heapq tutorial

# Leetcode - 152ms
# O(nklogk) runtime
# O(1) space
# divide and conquer using 2 way merge
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        start = 0
        end = len(lists) - 1
        return self.mergeK(lists, start, end)

    def mergeK(self, lists, start, end):
        if start > end:
            return None
        elif start == end:
            return lists[start]
        else:
            mid = start + (end - start ) / 2
            left = self.mergeK(lists, start, mid)
            right = self.mergeK(lists, mid + 1, end)
            return self.merge2(left, right)

    def merge2(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1:
            cur.next = l1
        elif l2:
            cur.next = l2
        return dummy.next

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

# O(nklogk) runtime
# O(1) space
# divide and conquer using 2 way merge
# Leetcode - OT
class Solution_dq:
    def mergeKLists(self, lists):
        if not lists:
            return lists
        begin, end = 1, len(lists) - 1

        f1 = lists[0]
        while begin < end:
            self.mergeTwoLists(f1, self.mergeTwoLists(lists[begin], lists[end]))
            begin += 1
            end -= 1
        return lists[0]

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1:
            cur.next = l1
        else:
            cur.next = l2

        return dummy.next

# O(nk log k) runtime,
# O(k) space - MinHeap/Priority queue
import unittest
# Leetcode - 148ms
class Solution(unittest.TestCase):
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        cur = dummy

        heap = []
        for sorted_list in lists:
            if sorted_list:
                heapq.heappush(heap, (sorted_list.val, sorted_list))

        while heap:
            smallest = heapq.heappop(heap)[1]
            cur.next = smallest
            cur = cur.next
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, smallest.next))
        return dummy.next

    def test(self):
        self.assertEqual()

if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(3)
    list2 = ListNode(2)
    list2.next = ListNode(4)

    print Solution().mergeKLists([list1, list2])
    print Solution_dq().mergeKLists([list1, list2])



#java
js = '''
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

 //use minHeap
 public class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) return null;
        PriorityQueue<ListNode> pq = new PriorityQueue<>((ListNode a, ListNode b) -> a.val - b.val);

        for (ListNode node : lists) { //adding the first node
             if (node!=null) pq.add(node);
        }

        ListNode dummy = new ListNode(0);
        ListNode tmp = dummy;
        while(!pq.isEmpty()) {
            tmp.next = pq.poll();
            tmp = tmp.next;

            if (tmp.next != null) {
                pq.offer(tmp.next);
            }
        }
        return dummy.next;
    }
}

 //idea of merge sort
public class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        return mergeKLists(lists, 0, lists.length - 1);
    }

    private ListNode mergeKLists(ListNode[] lists, int start, int end) {
        if (start > end) {
            return null;
        } else if (start == end) {
            return lists[start];
        } else {
            int mid = start + (end - start) / 2;
            ListNode list1 = mergeKLists(lists, start, mid);
            ListNode list2 = mergeKLists(lists, mid + 1, end);
            return merge(list1, list2);
        }
    }

    private ListNode merge(ListNode list1, ListNode list2) {
        ListNode fakeHead = new ListNode(0);
        ListNode cur = fakeHead;
        while (list1 != null && list2 != null) {
            if (list1.val <= list2.val) {
                cur.next = list1;
                list1 = list1.next;
            } else {
                cur.next = list2;
                list2 = list2.next;
            }
            cur = cur.next;
        }
        while (list1 != null) {
            cur.next = list1;
            list1 = list1.next;
            cur = cur.next;
        }
        while (list2 != null) {
            cur.next = list2;
            list2 = list2.next;
            cur = cur.next;
        }
        return fakeHead.next;
    }
}
'''