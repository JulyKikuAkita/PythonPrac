__source__ = 'https://leetcode.com/problems/next-closest-time/'
# Time:  O(1)
# Space: O(1)
#
# Description: Leetcode # 681. Next Closest Time
#
# Given a time represented in the format "HH:MM",
# form the next closest time by reusing the current digits.
# There is no limit on how many times a digit can be reused.
#
# You may assume the given input string is always valid.
# For example, "01:34", "12:09" are all valid.
# "1:34", "12:9" are all invalid.
#
# Example 1:
#
# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39,
# which occurs 5 minutes later.
# It is not 19:33, because this occurs 23 hours and 59 minutes later.
# Example 2:
#
# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
# It may be assumed that the returned time is next day's time
# since it is smaller than the input time numerically.
#
# Companies
# Google
# Related Topics
# String
#
# 269ms
import unittest
class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        return min((t <= time, t)
               for i in range(24 * 60)
               for t in ['%02d:%02d' % divmod(i, 60)]
               if set(t) <= set(time))[1]

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/next-closest-time/solution/
Since there are at max 4 * 4 * 4 * 4 = 256 possible times, just try them all...

# 3ms 94.77%
class Solution {
    public String nextClosestTime(String time) {
            String[] times = time.split(":");
            int hour = Integer.parseInt(times[0]);
            int minute = Integer.parseInt(times[1]);
            int[] digits = new int[4];
            digits[0] = hour%10;
            digits[1] = hour/10;
            digits[2] = minute%10;
            digits[3] = minute/10;
            int minLargerMinute = 60;
            int minLargerHour = 24;
            int minDigit = digits[0];
            for (int digit1 : digits) {
                minDigit = Math.min(minDigit, digit1);
                for (int digit2 : digits) {
                    int cand = digit1 * 10 + digit2;
                    if (cand > minute && cand < 60) {
                        minLargerMinute = Math.min(minLargerMinute, cand);
                    }
                    if (cand > hour && cand < 24) {
                        minLargerHour = Math.min(minLargerHour, cand);
                    }
                }
            }

            if(minLargerMinute != 60){
                return times[0]+":"+(minLargerMinute < 10?"0":"")+minLargerMinute;
            }

            if(minLargerHour != 24){
                return (minLargerHour <10 ?"0":"")+minLargerHour+":"+ (minDigit == 0? "00": (minDigit*10+ minDigit));
            }

            return minDigit == 0? "00:00": (minDigit*10+ minDigit)+":"+(minDigit*10+ minDigit);
        }
}

# 3ms 94.77%
class Solution {
    static int[] mins = { 600, 60, 10, 1 };
    public String nextClosestTime(String time) {
        int colon = time.indexOf(':');
        int cur = Integer.valueOf(time.substring(0, colon)) * 60 + Integer.valueOf(time.substring(colon + 1));
        char[] next = new char[4];
        for (int i = 1, d = 0; i <= 1440 && d < 4; i++) {
            int m = (cur + i) % 1440;
            for (d = 0; d < 4; d++) {
                next[d] = (char)('0' + m / mins[d]); m %= mins[d];
                if (time.indexOf(next[d]) == -1) break;
            }
        }
        return new String(next, 0, 2) + ':' + new String(next, 2, 2);
    }
}

'''
