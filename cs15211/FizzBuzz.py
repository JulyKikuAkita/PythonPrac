__source__ = 'https://leetcode.com/problems/fizz-buzz/'
# Time:  O(N)
# Space: O(1)
#
# Description: Leetcode # 412. Fizz Buzz
#
# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output "Fizz" instead of the number
# and for the multiples of five output "Buzz".
# For numbers which are multiples of both three and five output "FizzBuzz".
#
# Example:
#
# n = 15,
#
# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]
import unittest

# 48ms 46.39%
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        i = 1
        dict = ["Fizz", "Buzz"]
        ans = []
        while i <= n:
            if i % 15 == 0:
                #print dict[0]+dict[1]
                ans.append(dict[0]+dict[1])
            elif i % 3 == 0:
                #print dict[0]
                ans.append(dict[0])
            elif i % 5 == 0:
                #print dict[1]
                ans.append(dict[1])
            else:
                #print i
                ans.append(str(i))
            i += 1
        return ans


class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/fizz-buzz/solution/

# 1ms 100%
class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> ret = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            // if ((i+1)%3 == 0 && (i+1)%5 != 0) {
            //     ret.add("Fizz");
            // } else if ((i+1)%5 == 0 && (i+1)%3 != 0) {
            //     ret.add("Buzz");
            // } else if ((i+1)%5 == 0 && (i+1)%3 == 0) {
            //     ret.add("FizzBuzz");
            // } else {
            //     ret.add(Integer.toString(i+1));
            // }

            if ((i+1)%5 == 0 && (i+1)%3 == 0) {
                ret.add("FizzBuzz");
            } else if ((i+1)%5 == 0) {
                ret.add("Buzz");
            } else if ((i+1)%3 == 0) {
                ret.add("Fizz");
            } else {
                ret.add(Integer.toString(i+1));
            }
        }

        return ret;
    }
}
'''