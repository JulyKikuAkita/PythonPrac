__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/binary-watch.py
# Time:  O(1)
# Space: O(1)

# A binary watch has 4 LEDs on the top which represent the hours (0-11),
# and the 6 LEDs on the bottom represent the minutes (0-59).
#
# Each LED represents a zero or one, with the least significant bit on the right.
#
# For example, the above binary watch reads "3:25".
#
# Given a non-negative integer n which represents the number of LEDs that are currently on,
# return all possible times the watch could represent.
#
# Example:
#
# Input: n = 1
# Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
# Note:
# The order of output does not matter.
# The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
# The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
# Hide Company Tags Google
# Hide Tags Backtracking Bit Manipulation
# Hide Similar Problems (M) Letter Combinations of a Phone Number (E) Number of 1 Bits



class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        def bit_count(bits):
            count = 0
            while bits:
                bits &= bits-1
                count += 1
            return count

        return ['%d:%02d' % (h, m)
            for h in xrange(12) for m in xrange(60)
            if bit_count(h) + bit_count(m) == num]

    def readBinaryWatch2(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        return ['{0}:{1}'.format(str(h), str(m).zfill(2)) for h in range(12) for m in range(60) if (bin(h) + bin(m)).count('1') == num]

    def readBinaryWatch2(self, num):
        return ['%d:%02d' % (h, m)
            for h in range(12) for m in range(60)
            if (bin(h) + bin(m)).count('1') == num]

'''
public class Solution {
    public List<String> readBinaryWatch(int num) {
         List<String> times = new ArrayList<>();
        for (int h=0; h<12; h++)
            for (int m=0; m<60; m++)
                if (Integer.bitCount(h * 64 + m) == num)
                    times.add(String.format("%d:%02d", h, m));
        return times;
    }
}
'''