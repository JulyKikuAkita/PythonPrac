__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/recover-binary-search-tree.py
# Time:  O(n)
# Space: O(1)
# Tree
#
# Two elements of a binary search tree (BST) are swapped by mistake.
#
# Recover the tree without changing its structure.
#
# Note:
# A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
#

# http://www.cnblogs.com/zuoyuan/p/3746594.html
# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

     def __repr__(self):
         if self:
             serial = []
             queue = [self]

             while queue:
                 cur = queue[0]

                 if cur:
                     serial.append(cur.val)
                     queue.append(cur.left)
                     queue.append(cur.right)
                 else:
                     serial.append("#")

                 queue = queue[1:]

             while serial[-1] == "#":
                 serial.pop()
             # print "test: ", str(serial), repr(serial) repr() ~= str()
             return repr(serial)
         else:
             return None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        return self.MorrisTraversal(root)

    # as BST inorder
    def MorrisTraversal(self, root):
        if root is None:
            return
        broken = [None, None]
        pre, cur = None, root # cur is pre's right child

        while cur:
            #1) no left child
            if cur.left is None:
                self.detectBroken(broken, pre,cur)
                pre= cur
                cur = cur.right

            #2) left child's right most leaf
            else:
                node = cur.left
                while node.right and node.right != cur:
                    node = node.right

            #3) no right child
                if node.right == None:
                    node.right = cur
                    cur = cur.left

            #4) has right child
                else:
                    self.detectBroken(broken, pre, cur)
                    node.right = None
                    pre = cur
                    cur = cur.right

        broken[0].val, broken[1].val = broken[1].val, broken[0].val
        return root

    def detectBroken(self, broken, pre, cur):
        if pre and pre.val > cur.val:
            if broken[0] is None:
                broken[0] = pre
            broken[1] = cur




class SolutionOther:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        self.n1 = self.n2 = None
        self.prev = None
        self.findTwoNodes(root)
        self.n1.val, self.n2.val = self.n2.val, self.n1.val
        return root


    def findTwoNodes(self, root):
        if root:
            self.findTwoNodes(root.left)
            if self.prev and self.prev.val > root.val:
                self.n2 = root
                if self.n1 == None:
                    self.n1 = self.prev
            self.prev = root
            self.findTwoNodes(root.right)


    def inorder(self, root, list, listp):
        if root:
            self.inorder(root.left, list, listp)
            list.append(root.val)
            listp.append(root)
            self.inorder(root.right, list, listp)

    def recoverTreeON(self, root):
        list = []
        listp = []
        self.inorder(root, list, listp)
        list.sort()
        for i in range(len(list)):
            listp[i].val = list[i]
        return root


#create tree
root1=TreeNode(0)
root2=TreeNode(1)
root3=TreeNode(3)
root4=TreeNode(4)
root5=TreeNode(5)

tree2=TreeNode(2)
tree31=TreeNode(5)
tree32=TreeNode(2)
tree41=TreeNode(4)
tree411=TreeNode(4)
tree4111=TreeNode(4)
tree51=TreeNode(1)
tree52=TreeNode(2)
tree511=TreeNode(3)
tree522=TreeNode(4)
tree5221=TreeNode(5)
tree52212=TreeNode(6)

root2.left=tree2

root3.left=tree31
root3.right=tree32

root4.right =tree41
tree41.right=tree411
tree411.right=tree4111

root5.left=tree51
root5.right=tree52
tree51.left=tree511
tree52.right=tree522
tree522.left=tree5221
tree5221.right=tree52212

my_test=SolutionOther()
#print root5
print my_test.recoverTree(root5)

# test
if __name__ == "__main__":
    root = TreeNode(0)
    root.left = TreeNode(1)
    print root3
    print Solution().recoverTree(root3)

#java
js = '''
public class Solution {
    private TreeNode pre;
    private TreeNode fir;
    private TreeNode sec;

    public void recoverTree(TreeNode root) {
        pre = null;
        fir = null;
        sec = null;
        inorder(root);
        int tmp = fir.val;
        fir.val = sec.val;
        sec.val = tmp;
    }

    private void inorder(TreeNode root){
        if (root == null) return ;
        inorder(root.left);
        if ( pre == null ) {
            pre = root;
        }else{
            if (pre.val > root.val) {
                if (fir == null) {
                    fir = pre;
                }
                sec = root;
            }
            pre = root;
        }
        inorder(root.right);
    }
}
'''