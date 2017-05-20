__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/missing-ranges.py
# Time:  O(n)
# Space: O(1)
#
# Given a sorted integer array where the range of elements are [lower, upper] inclusive,
# return its missing ranges.
#
# For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# return ["2", "4->49", "51->74", "76->99"].
#
# Google
class Solution:
    # @param A, a list of integers
    # @param lower, an integer
    # @param upper, an integer
    # @return a list of strings
    def findMissingRanges(self, A, lower, upper):
        ranges = []
        pre = lower - 1

        for i in xrange(len(A) + 1):
            if i == len(A):
                cur = upper + 1
            else:
                cur = A[i]

            if cur - pre >= 2:
                ranges.append(self.getRange(pre + 1, cur - 1))

            pre = cur

        return ranges

    def getRange(self, lower, upper):
        if lower == upper:
            return "{}".format(lower)
        else:
            return "{}->{}".format(lower, upper)

#test
if __name__ == "__main__":
    arr = [0, 1, 3, 50, 75]
    print Solution().findMissingRanges(arr,0, 99)

#java
js = '''
public class Solution {
    public List<String> findMissingRanges(int[] nums, int lower, int upper) {
        List<String> result = new ArrayList<>();
        int cur = lower;
        for (int num : nums) {
            if (cur < num) {
                result.add(convertToString(cur, num - 1));
                cur = num;
            } else if (cur > num) {
                continue;
            }
            cur++;
        }
        if (cur != upper + 1) {
            result.add(convertToString(cur, upper));
        }
        return result;
    }

    private String convertToString(int lower, int upper) {
        StringBuilder sb = new StringBuilder();
        sb.append(lower);
        if (upper != lower) {
            sb.append("->");
            sb.append(upper);
        }
        return sb.toString();
    }
}
'''