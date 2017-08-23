__source__ = 'https://leetcode.com/problems/russian-doll-envelopes/description/'
# https://github.com/kamyu104/LeetCode/blob/master/Python/russian-doll-envelopes.py
# Time:  O(nlogn + nlogk) = O(nlogn), k is the length of the result.
# Space: O(1)
#
# Description: Leetcode # 354. Russian Doll Envelopes
#
# You have a number of envelopes with widths and heights given
# as a pair of integers (w, h). One envelope can fit into another
# if and only if both the width and height of one envelope is greater
# than the width and height of the other envelope.
#
# What is the maximum number of envelopes can you Russian doll?
# (put one inside other)
#
# Example:
# Given envelopes = [[5,4],[6,4],[6,7],[2,3]], the maximum number
# of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
#
# Companies
# Google
# Related Topics
# Binary Search Dynamic Programming
# Similar Questions
# Longest Increasing Subsequence
#
import unittest
class Solution(unittest.TestCase):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def insert(target):
            left, right = 0, len(result) - 1
            while left <= right:
                mid = left + (right - left) / 2
                if result[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            if left == len(result):
                result.append(target)
            else:
                result[left] = target

        result = []

        envelopes.sort(lambda x, y: y[1] - x[1] if x[0] == y[0] else \
                                    x[0] - y[0])
        for envelope in envelopes:
            insert(envelope[1])

        return len(result)
    def test(self):
        arr = [[1,2],[2,3],[3,4],[3,5],[4,5],[5,5],[5,6],[6,7],[7,8]]
        self.assertEqual(self.maxEnvelopes(arr), 7)

class Solution2(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        def bin_search(target):
            left, right = 0, len(res) - 1
            while left + 1 < right:
                mid = left + (right - left) / 2
                if res[mid] < target:
                    left = mid
                else:
                    right = mid
            if len(res) == 0 or res[right] < target:
                res.append(target)
            elif res[left] < target:
                res[right] = target
            else:
                res[left] = target
        res = []
        envelopes.sort(lambda x, y : x[0] - y[0] if x[0] != y[0] else y[1] - x[1])
        print envelopes
        for envelope in envelopes:
            bin_search(envelope[1])
        return len(res)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)

if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought:
Sort the array. Ascend on width and descend on height if width are same.
Find the longest increasing subsequence based on height.
Since the width is increasing, we only need to consider height.
[3, 4] cannot contains [3, 3], so we need to put [3, 4]
before [3, 3] when sorting otherwise it will be counted as an increasing number if the order is [3, 3], [3, 4]

#97.15% 18ms
public class Solution {
    public int maxEnvelopes(int[][] envelopes) {
        if(envelopes == null || envelopes.length == 0
           || envelopes[0] == null || envelopes[0].length != 2)
            return 0;
        Arrays.sort(envelopes, new Comparator<int[]>(){
            public int compare(int[] arr1, int[] arr2){
                if(arr1[0] == arr2[0])
                    return arr2[1] - arr1[1];
                else
                    return arr1[0] - arr2[0];
           }
        });
        int dp[] = new int[envelopes.length];
        int len = 0;
        for(int[] envelope : envelopes){
            int index = Arrays.binarySearch(dp, 0, len, envelope[1]);
            if(index < 0)
                index = -(index + 1);
            dp[index] = envelope[1];
            if(index == len)
                len++;
        }
        return len;
    }
}

#64.69% 83ms
public class Solution {
    public int maxEnvelopes(int[][] envelopes) {
        if ( envelopes.length < 2) return envelopes.length;
        int[] arr = new int[envelopes.length];
        int tail = -1;
        Arrays.sort(envelopes, (o1, o2) -> o1[0] != o2[0]? o1[0]-o2[0] : o2[1] - o1[1]); //have o2 - o1 so that if x is same, bigger y first

        for( int[] envelope : envelopes) {
            //System.out.println(tail +" " + envelope[0] + " " + envelope[1]);
            if ( tail == -1 || arr[tail] < envelope[1] ) {
                arr[++tail] = envelope[1];
            } else{
                int idx = findFirstLargerOrEqual(arr, 0, tail, envelope[1]);
                arr[idx] = envelope[1];
            }
        }
        return tail + 1;
    }

    private int findFirstLargerOrEqual(int[] arr, int start, int end, int num) {
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            if (arr[mid] < num) {
                start = mid;
            }else{
                end = mid;
            }
        }

        return arr[start] < num ? end: start;
    }

}

#test:
[[1,2],[2,3],[3,4],[3,5],[4,5],[5,5],[5,6],[6,7],[7,8]]
-> the sorting order is: [[1,2],[2,3],[3,5],[3,4],[4,5],[5,6],[5,5],[6,7],[7,8]]
'''