__source__ = 'https://leetcode.com/problems/number-of-longest-increasing-subsequence/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 673. Number of Longest Increasing Subsequence
#
# Given an unsorted array of integers, find the number of longest increasing subsequence.
#
# Example 1:
# Input: [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
# Example 2:
# Input: [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
# Note: Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.
#
# Related Topics
# Dynamic Programming Facebook
# Similar Questions
# Longest Increasing Subsequence Longest Continuous Increasing Subsequence
#
import unittest


class Solution(object):
    pass  # your function here


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/number-of-longest-increasing-subsequence/solution/

# 19ms 96.81%
class Solution {
    public int findNumberOfLIS(int[] nums) {
        int len = nums.length;
        int[] dp = new int[len];
        int[] count = new int[len];
        int max = 1;
        Arrays.fill(dp, 1);
        Arrays.fill(count, 1);
        for (int i = 0; i < len; i++) {
            for (int j = i - 1; j >= 0; j--) {
                if (nums[j] < nums[i]) {
                    if (dp[j] + 1 > dp[i]) {
                        dp[i] = dp[j] + 1;
                        count[i] = count[j];
                    } else if (dp[j] + 1 == dp[i]) {
                        count[i] += count[j];
                    }
                    max = Math.max(max, dp[i]);
                }
            }
        }
        int res = 0;
        for (int i = 0; i < len; i++) {
            if (dp[i] == max) {
                res += count[i];
            }
        }
        return res;
    }
}

# 11ms 100%
class Solution {
    public int findNumberOfLIS(int[] nums) {
        if(nums==null||nums.length==0)return 0;
        Node[] nodes=new Node[nums.length];
        nodes[0]=new Node(nums[0],1,null);
        int idx=0;
        for(int i=1;i<nums.length;i++){
            if(nums[i]>nodes[idx].num){
                int sum=0;
                Node node=nodes[idx];
                while(node!=null&&node.num<nums[i]){
                    sum+=node.cnt;
                    node=node.next;
                }
                nodes[++idx]=new Node(nums[i],sum,null);
            }else {
                int index=get(nodes,idx+1,nums[i]);
                int sum=0;
                if(index==0)sum=1;
                else{
                    Node node=nodes[index-1];
                    while(node!=null&&node.num<nums[i]){
                        sum+=node.cnt;
                        node=node.next;
                    }
                    
                }
                Node tmp=new Node(nums[i],sum,nodes[index]);
                    nodes[index]=tmp;
            }
        }
        int res=0;
        Node node=nodes[idx];
        while(node!=null){
            res+=node.cnt;
            node=node.next;
        }
        return res;
    }
    public int get(Node[] nodes,int last,int target){
        int left=0,right=last;
        while(left<right){
            int mid=(left+right)/2;
            if(nodes[mid].num<target)left=mid+1;
            else right=mid;
        }
        return left;
    }
}
class Node{
    int num,cnt;
    Node next;
    Node(){
        num=0;
        cnt=0;
        next=null;
    }
    Node(int n,int c,Node ne){
        num=n;
        cnt=c;
        next=ne;
    }
}
'''
