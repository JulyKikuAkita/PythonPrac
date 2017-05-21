
__source__ = 'https://leetcode.com/problems/student-attendance-record-i/#/description'
# Time:  O()
# Space: O()
#
# Description:
#
# You are given a string representing an attendance record for a student.
# The record only contains the following three characters:
#
# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent)
# or more than two continuous 'L' (late).
#
# You need to return whether the student could be rewarded according to his attendance record.
#
# Example 1:
# Input: "PPALLP"
# Output: True
# Example 2:
# Input: "PPALLL"
# Output: False
#
# Hide Company Tags Google
# Hide Tags String
# Hide Similar Problems (H) Student Attendance Record II

import unittest
import re
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return re.match('.*LLL.*|.*A.*A.*', s) == None #if no match, return None

# your function here

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertFalse(Solution().checkRecord("PPALLL"))
        self.assertTrue(Solution().checkRecord("PPALLP"))


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/articles/student-attendance-record-i/

public class Solution {
    public boolean checkRecord(String s) {
        if(s.indexOf("A") != s.lastIndexOf("A") || s.contains("LLL"))
            return false;
        return true;
    }

    public boolean checkRecord2(String s) {
    return !s.matches(".*LLL.*|.*A.*A.*");
}
}
'''