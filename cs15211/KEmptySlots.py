__source__ = 'https://leetcode.com/problems/k-empty-slots/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 683. K Empty Slots
#
#There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days.
# In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.
#
# Given an array flowers consists of number from 1 to N.
# Each number in the array represents the place where the flower will open in that day.
#
# For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x,
# where i and x will be in the range from 1 to N.
#
# Also given an integer k, you need to output in which day there exists two flowers in the status of blooming,
# and also the number of flowers between them is k and these flowers are not blooming.
#
# If there isn't such day, output -1.
#
# Example 1:
# Input:
# flowers: [1,3,2]
# k: 1
# Output: 2
# Explanation: In the second day, the first and the third flower have become blooming.
#
# Example 2:
# Input:
# flowers: [1,2,3]
# k: 1
# Output: -1
# Note:
# The given array will be in the range [1, 20000].
#
# Companies
# Google
# Related Topics
# Array
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
#Thought:
It seems that this question has some mistakes. I think there are two places that might lead to misunderstandings:
(please feel free to tell me if I'm incorrect)

flowers[i] = x should mean that the unique flower that blooms at day i+1 (not i) will be at position x.
If you can get multiple possible results, then you need to return the minimum one.
The idea is to use an array days[] to record each position's flower's blooming day.
That means days[i] is the blooming day of the flower in position i+1.
We just need to find a subarray days[left, left+1,..., left+k-1, right] which satisfies:
for any i = left+1,..., left+k-1, we can have days[left] < days[i] && days[right] < days[i].
Then, the result is max(days[left], days[right]).

#42.98% 127ms
class Solution {
    public int kEmptySlots(int[] flowers, int k) {
        TreeSet<Integer> blooming = new TreeSet<>();
        int day = 0;

        for (int slot: flowers) {
            day++;
            blooming.add(slot);
            for (Integer neighbor : new Integer[]{blooming.lower(slot), blooming.higher(slot)}){
                if (neighbor != null && Math.abs(neighbor - slot) - 1 == k) return day;
            }
        }
        return -1;
    }
}
#99.48% 13ms
class Solution {
    public int kEmptySlots(int[] flowers, int k) {
        if(k < 0 || k > flowers.length - 2) {
            return -1;
        }
        k++;
        int[] mins = new int[flowers.length / k + 3];
        int[] maxs = new int[mins.length];
        Arrays.fill(mins, Integer.MAX_VALUE);
        Arrays.fill(maxs, Integer.MIN_VALUE);
        for(int i = 0; i < flowers.length; i++) {
            int flower = flowers[i];
            int index = flower / k + 1;
            if(flower < mins[index]) {
                mins[index] = flower;
                if(maxs[index - 1] + k == flower) {
                    return i + 1;
                }
            }
            if(flower > maxs[index]) {
                maxs[index] = flower;
                if(flower + k == mins[index + 1]) {
                    return i + 1;
                }
            }
        }
        return -1;
    }
}
'''