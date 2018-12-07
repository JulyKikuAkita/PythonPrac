__source__ = 'https://leetcode.com/problems/car-fleet/'
# Time:  O(NlogN)
# Space: O(N)
#
# Description: Leetcode # 853. Car Fleet
#
# N cars are going to the same destination along a one lane road.
# The destination is target miles away.
#
# Each car i has a constant speed speed[i] (in miles per hour),
# and initial position position[i] miles towards the target along the road.
#
# A car can never pass another car ahead of it,
# but it can catch up to it, and drive bumper to bumper at the same speed.
#
# The distance between these two cars is ignored - they are assumed to have the same position.
#
# A car fleet is some non-empty set of cars driving at the same position and same speed.
# Note that a single car is also a car fleet.
#
# If a car catches up to a car fleet right at the destination point,
# it will still be considered as one car fleet.
# How many car fleets will arrive at the destination?
#
# Example 1:
#
# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Output: 3
# Explanation:
# The cars starting at 10 and 8 become a fleet, meeting each other at 12.
# The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
# The cars starting at 5 and 3 become a fleet, meeting each other at 6.
# Note that no other cars meet these fleets before the destination, so the answer is 3.
#
# Note:
#
# 0 <= N <= 10 ^ 4
# 0 < target <= 10 ^ 6
# 0 < speed[i] <= 10 ^ 6
# 0 <= position[i] < target
# All initial positions are different.
#
import unittest

# 68ms 68.15%
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        cars = sorted(zip(position, speed))
        times = [float(target - p) / s for p, s in cars]
        ans = 0
        while len(times) > 1:
            lead = times.pop()
            if lead < times[-1]: ans += 1  # if lead arrives sooner, it can't be caught
            else: times[-1] = lead # else, fleet arrives at later time 'lead'
        return ans + bool(times) # remaining car is fleet (if it exists)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
# Thought: https://leetcode.com/problems/car-fleet/solution/
Approach 1: Stack
Complexity Analysis
Time Complexity: O(NlogN), where N is the number of cars. The complexity is dominated by the sorting operation.
Space Complexity: O(N), the space used to store information about the cars.

# 62ms 38.12%
class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int N = position.length;
        Car[] cars = new Car[N];
        for (int i = 0; i < N; i++) {
            cars[i] = new Car(position[i], (double) (target - position[i]) / speed[i]);
        }
        Arrays.sort(cars, (a, b) -> Integer.compare(a.position, b.position));

        int ans = 0, t = N;
        while (--t > 0) {
            if (cars[t].time < cars[t - 1].time) ans++; //if cars[t] arrives sooner, it can't be caught
            else cars[t - 1] = cars[t]; //else, cars[t-1] arrives at same time as cars[t]
        }
        return ans + (t == 0 ? 1 : 0); //lone car is fleet (if it exists)
    }

    class Car {
        int position;
        double time;
        Car(int p, double t) {
           position = p;
            time = t;
        }
    }
}

# faster sorting on the position, and build the relation between pos/speed
# 12ms 100%
class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        int count = 0;
        int[] p = new int[target + 1];
        for (int i = 0; i < position.length; i++) {
            p[position[i]] = speed[i];
        }

        double sp = 0;
        for (int i = target; i >= 0; i--) {
            if (p[i] != 0) {
                double slow = (double) (target - i) / p[i];
                if (slow > sp) {
                    count++;
                    sp = slow;
                }
            }
        }
        return count;
    }
}

# map
# 19ms 98.85%
class Solution {
    public int carFleet(int target, int[] position, int[] speed) {
        if(position == null || position.length == 0) return 0;
        HashMap<Integer, Integer> hm = new HashMap();
        for (int i = 0; i < position.length; i++) {
            hm.put(position[i], speed[i]);
        }
        Arrays.sort(position);
        int res = 1;
        int index = position.length - 1;
        double time = (target - position[index]) * 1.0 / hm.get(position[index]);
        for (int i = position.length - 2; i >= 0; i--) {
            double newTime = (target - position[i]) * 1.0 / hm.get(position[i]);
            if (newTime > time) { //arrive seperately
                res++;
                time = newTime;
            }
        }
        return res;
    }
}
'''