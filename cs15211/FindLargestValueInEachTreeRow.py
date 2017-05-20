from TreeSerizalize import drawtree, deserialize

__author__ = 'July'
#You need to find the largest value in each row of a binary tree.
#
#
#Example:
# Input:
#
#          1
#         / \
#        3   2
#       / \   \
#      5   3   9
#
#Output: [1, 3, 9]
#Hide Company Tags LinkedIn
#Hide Tags Tree Depth-first Search Breadth-first Search
#
# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.list = [root.val]
        self.helper(root, 0)
        return self.list

    def helper(self, root, depth):
        if not root:
            return
        if len(self.list) < depth + 1:
            self.list.append(float('-inf'))
        if root.val > self.list[depth]:
            self.list[depth] = root.val

        self.helper(root.left, depth + 1)
        self.helper(root.right, depth + 1)


class SolutionFastest(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        maxs=[]
        lever=[root]
        while any(lever):
            maxs.append(max([node.val for node in lever]))
            lever = [kid for node in lever for kid in (node.left,node.right) if kid]

        return maxs

class Solution2(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        level = [root]
        res = []
        while level:
            res.append(max(i.val for i in level))
            temp = level
            level = []
            for i in temp:
                if i.left:
                    level.append(i.left)
                if i.right:
                    level.append(i.right)
        return res

#test
if __name__ == "__main__":
    #root1 = drawtree(deserialize('[1,2,3,null,null,4,null,null,5]'))
    #root2 = drawtree(deserialize('[1,3,2,5,3,null,9]'))

    print Solution().largestValues(drawtree(deserialize('[0,-1]')))
    #print Solution().largestValues(root2)

'''
public class Solution {
    public List<Integer> largestValues(TreeNode root) {
        List<Integer> res = new ArrayList<Integer>();
        helper(root, res, 0);
        return res;
    }
    private void helper(TreeNode root, List<Integer> res, int d){
        if(root == null){
            return;
        }
       //expand list size
        if(d == res.size()){
            res.add(root.val);
        }
        else{
        //or set value
            res.set(d, Math.max(res.get(d), root.val));
        }
        helper(root.left, res, d+1);
        helper(root.right, res, d+1);
    }
}

Verbose Java Solution, Binary tree level order traversal, again.
Alright, two binary tree level order traversal problems in one contest. This time, mission is to find the max of each level...

public class Solution {
    public int[] findValueMostElement(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        if (root == null) return new int[0];

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            int size = queue.size();
            int max = Integer.MIN_VALUE;
            for (int i = 0; i < size; i++) {
                TreeNode node = queue.poll();
                max = Math.max(max, node.val);
                if (node.left != null) queue.add(node.left);
                if (node.right != null) queue.add(node.right);
            }
            res.add(max);
        }

        int[] result = new int[res.size()];
        for (int i = 0; i < res.size(); i++) {
            result[i] = res.get(i);
        }

        return result;
    }
}
'''