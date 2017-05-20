__author__ = 'July'
# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
class Namespace: pass
class Solution:
    # @param root, a tree node
    # @return a boolean
    #use global var
    def isBalanced3(self, root):

        def dfs(root):
            global ans
            ans = True
            if root == None:
                return 0
            ltval = dfs(root.left)
            rtval = dfs(root.right)
            if  not (ltval - rtval <= 1 and ltval - rtval >= -1):
                ans = False
            print root.val, ans
            return max(ltval, rtval) +1

        dfs(root)
        return ans

    #use name space as described in #7 from http://www.saltycrane.com/blog/2008/01/python-variable-scope-notes/
    def isBalanced2(self, root):
        ns = Namespace()
        ns.ans = True


        def dfs2(root):
            if root == None:
                return 0
            ltval = dfs2(root.left)
            rtval = dfs2(root.right)
            if  not (ltval - rtval <= 1 and ltval - rtval >= -1):
                ns.ans = False
            print root.val, ns.ans
            return max(ltval, rtval) +1


        dfs2(root)
        return ns.ans

#############test
#creating BST tree ####
root0=TreeNode(0)
tree1=TreeNode(1)
tree2=TreeNode(2)
tree3=TreeNode(3)
tree4=TreeNode(4)
tree5=TreeNode(5)
tree6=TreeNode(6)
root0.left=tree1
#root0.right=tree2
tree1.left=tree3
tree1.right=tree4
tree2.left=tree5
#tree2.right=tree6
#end of creating BST tree ####
#test
test = Solution()
print test.isBalanced(root0)
#print test.isBalanced3(root0)
#print test.isBalanced2(root0)