__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/copy-list-with-random-pointer.py
# Time:  O(n)
# Space: O(1)
# LinkedList
#
# A linked list is given such that each node contains an additional random pointer
# which could point to any node in the list or null.
#
# Return a deep copy of the list.
# Hash Table Linked List
# Amazon, Bloomberg, Microsoft, Uber

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        # copy and combine copied list with original list
        current = head
        while current:
            tmp = RandomListNode(current.label)
            tmp.next = current.next
            current.next = tmp
            current = current.next

        # update random node in copied list
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        # split copied list from combined one
        dummy = RandomListNode(0)
        copied, current = dummy, head
        while current:
            copied.next = current.next
            current.next = current.next.next
            copied, current = copied.next, current.next
        return dummy.next



# Time:  O(n)
# Space: O(n) dict
class Solution2:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        dummy = RandomListNode(0)
        cur, prev = head, dummy
        dict = {}

        #traverse original list to create hashtable
        while cur:
            copied = RandomListNode(cur.label)
            dict[cur] = copied
            #copied.random = cur.random # this line fail - Random pointer points to a node from the original list.
            prev.next = copied
            prev, cur = prev.next, cur.next

        #traverse copied node to make random pointer copy (not a ptr to original list)
        cur = head
        while cur:
            if cur.random:
                dict[cur].random = dict[cur.random] # make random node point to copied list
            cur= cur.next

        return dummy.next


if __name__ == "__main__":
    head = RandomListNode(1)
    head.next = RandomListNode(2)
    head.random = head.next
    result = Solution().copyRandomList(head)
    print result.label
    print result.next.label
    print result.random.label


# http://www.cnblogs.com/zuoyuan/p/3745126.html
class SolutionOther:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head == None:
            return head
        tmp = head
        while tmp:
            newNode = RandomListNode(tmp.label)
            newNode.next = tmp.next
            tmp.next = newNode
            tmp = tmp.next.next

        tmp = head
        while tmp:
            if tmp.random:
                tmp.next.random = tmp.random.next
            tmp = tmp.next.next

        newhead = head.next
        pold = head
        pnew = newhead

        while pnew.next:
            pold.next = pnew.next
            pold = pold.next
            pnew.next = pold.next
            pnew =pnew.next

        pold.next = None
        pnew.next = None
        return newhead
#test
c1 = RandomListNode(3) ; c2 = RandomListNode(7) ; c3 = RandomListNode(4) ; c4 = RandomListNode(9) ; c5 = RandomListNode(5); c6 = RandomListNode(2);c7 = RandomListNode(6); c8 = RandomListNode(1)
c1.next = c2 ; c2.next = c3 ; c3.next = c4; c4.next = c5; c5.next = c6 ; c6.next = c7 ; c7.next = c8

test = SolutionOther()
nh = test.copyRandomList(c1)

while nh:
    print nh.label, nh.__class__
    nh = nh.next

print "\n original list \n"
while c1:
    print c1.label, c1.__class__
    c1= c1.next

#java
js = '''
/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        if( head == null) return head;
        RandomListNode cur = head;

        while(cur != null){
            RandomListNode next = cur.next;
            RandomListNode newCur = new RandomListNode(cur.label);
            cur.next = newCur;
            newCur.next = next;
            cur = next;
        }

        cur = head;
        while(cur != null){
            if(cur.random != null){
                cur.next.random = cur.random.next;
            }
            cur = cur.next.next;
        }
        cur = head;
        RandomListNode newHead = cur.next;
        while(cur != null){
            RandomListNode next = cur.next.next;
            RandomListNode newNext = next == null ? null : next.next;
            cur.next.next = newNext;
            cur.next = next;
            cur = next;
        }
        return newHead;
    }
}
'''
