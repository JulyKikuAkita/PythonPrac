__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/convert-sorted-list-to-binary-search-tree.py

# Time:  O(n)
# Space: O(logn)
# Divide and Conquer
#
# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
#

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None
# http://www.programcreek.com/2013/01/leetcode-convert-sorted-list-to-binary-search-tree-java/
# you need to create nodes bottom-up, and assign them to its parents.
# The bottom-up approach enables us to access the list in its order at the same time as creating nodes.
class Solution:
    head = None
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        current, length = head, 0
        while current != None: # get list length
            current, length = current.next, length + 1
        self.head = head
        return self.sortedListToBSTRecu(0, length - 1)
    # build tree bottom-up
    def sortedListToBSTRecu(self, start, end):
        if start > end:
            return
        mid = (start + end ) / 2
        left = self.sortedListToBSTRecu(start, mid - 1)
        current = TreeNode(self.head.val)
        current.left = left
        self.head = self.head.next
        current.right = self.sortedListToBSTRecu(mid + 1, end)
        return current

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    result = Solution().sortedListToBST(head)
    print result.val
    print result.left.val
    print result.right.val

class SolutionOther:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        listlen =0
        p = head
        while (p != None):
            p = p.next
            listlen += 1

        return self.dfs(head, listlen)

    def dfs(self, head, listlen):
        if listlen <= 0:
            return None

        mint, i = (listlen+1)/2 , 1
        #print mint
        midnode = head
        while (i < mint):
            midnode = midnode.next
            i += 1

        node = TreeNode(midnode.val)
        print node.val, mint, listlen
        node.left = self.dfs(head, mint - 1)
        node.right = self.dfs(midnode.next, listlen-mint)

        return node

    def preorderTraversal1(self, root):
        allnodes = []
        p =root

        def preorder(p, ans):
            if p is None:
                return
            ans += [p.val]
            if p.left != None:
                preorder(p.left, ans)

            if p.right != None:
                preorder(p.right, ans)

        preorder(p,allnodes)
        return allnodes


#test
#creating sort list#
n0 = ListNode(0)
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
p0 = ListNode(0)
p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p0.next = p1
p1.next = p2
p2.next = p3
#end of creating sort list#
test = Solution()

#node = test.sortedListToBST(n0)
#print test.preorderTraversal1(node)
nodep = test.sortedListToBST(p0)
#print test.preorderTraversal1(nodep)

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
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    private ListNode node;

    public TreeNode sortedListToBST(ListNode head) {
        if (head == null) {
            return null;
        }
        int len = getLength(head);
        node = head;
        return sortedListToBST(0, len - 1);
    }

    private TreeNode sortedListToBST(int start, int end) {
        if (start > end) {
            return null;
        }
        int mid = start + (end - start) / 2;
        TreeNode left = sortedListToBST(start, mid - 1);
        TreeNode root = new TreeNode(node.val);
        node = node.next;
        TreeNode right = sortedListToBST(mid + 1, end);
        root.left = left;
        root.right = right;
        return root;
    }

    private int getLength(ListNode head) {
        int length = 0;
        while (head != null) {
            length++;
            head = head.next;
        }
        return length;
    }
}
'''