__source__ = 'https://leetcode.com/problems/maximum-depth-of-binary-tree/#/description'
# https://github.com/kamyu104/LeetCode/blob/master/Python/maximum-depth-of-binary-tree.py
# Time:  O(n)
# Space: O(h), h is height of binary tree
#
# Given a binary tree, find its maximum depth.
#
# The maximum depth is the number of nodes along the longest path
# from the root node down to the farthest leaf node.
#
#  Depth-first Search
# You might like:
# (E) Balanced Binary Tree (E) Minimum Depth of Binary Tree
# Company:
# LinkedIn Uber Apple Yahoo


# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root == None:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1



class SolutionOther:
    # @param root, a tree node
    # @return an integer
    def maxDepthtoFix1(self, root):
        count =[0]

        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        else:
            def deepestNodeToFix(leafnode):

                if leafnode == None:
                    return
                if leafnode.left == None and leafnode.right == None:
                    return
                else:
                     # balanced tree count needs to -1
                    deepestNodeToFix(leafnode.right)
                    print "mid left", count[0]
                    deepestNodeToFix(leafnode.left)
                    print "mid right", count[0]
                    count[0] += 1
                    print "last", count[0]

                return count[0]

            # need to add root node
        return  deepestNodeToFix(root)+1

    def maxDepthtoFix2(self, root):
        lcount =[0]
        rcount =[0]

        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        else:
            def deepestNode2(leafnode):

                if leafnode== None:
                    return

                if leafnode.left != None:
                    deepestNode2(leafnode.left)
                    lcount[0] += 1
                    print "left" , lcount[0],rcount[0]

                if leafnode.right != None:
                    deepestNode2(leafnode.right)
                    rcount[0] += 1
                    print "right" ,lcount[0],rcount[0]

               # return the deepest leaf count
                if lcount[0] >= rcount[0]:
                    return lcount[0]
                else :
                    return rcount[0]
        return  deepestNode2(root)+1


    def maxDepth(self, root):
        count =[0]
        max=[0]

        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return 1
        else:
            def deepestNode(leafnode):

                if count[0] > max[0]:
                    print "cmp", max, count[0]
                    max[0] = count[0]

                if leafnode== None :
                    return

                if leafnode.right != None:
                    count[0] += 1
                    print "start right", count[0]
                    deepestNode(leafnode.right)
                    count[0] -= 1
                    print "mid right", count[0]
                if leafnode.left != None:
                    count[0] += 1
                    print "start left", count[0]
                    deepestNode(leafnode.left)
                    count[0] -= 1
                    print "mid left", count[0]



                print "last", max, count[0]
                return max[0]

        # need to add root node
        return  deepestNode(root)+1

#create tree
root1=TreeNode(0)
root2=TreeNode(1)
root3=TreeNode(2)
root4=TreeNode(4)
root5=TreeNode(5)

tree2=TreeNode(2)
tree31=TreeNode(3)
tree32=TreeNode(3)
tree41=TreeNode(4)
tree411=TreeNode(4)
tree4111=TreeNode(4)
tree51=TreeNode(5)
tree52=TreeNode(5)
tree511=TreeNode(5)
tree522=TreeNode(5)
tree5221=TreeNode(5)
tree52212=TreeNode(5)

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
#print my_test.maxDepth(root1)
#print my_test.maxDepth(root2)
#print my_test.maxDepth(root3)
#print my_test.maxDepth(root4)
print my_test.maxDepth(root5)
#print my_test.maxDepthtoFix2(root5)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    print Solution().maxDepth(root5)

#Java
java = '''

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

#DFS: 16%
public class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}

#DFS: 96%
public class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null){ return 0; }
        int l = 1 + maxDepth(root.left);
        int r = 1 + maxDepth(root.right);
        if (l > r){ return l; }
        return r;
    }
}

#BFS: 4.3%
public class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        int res = 0;
        while (!q.isEmpty()) {
            int len = q.size();
            for (int i = 0; i < len; i++) {
                TreeNode cur = q.poll();
                if (cur.left != null) q.offer(cur.left);
                if (cur.right != null) q.offer(cur.right);
            }
            res++;
        }
        return res;
    }
}
'''