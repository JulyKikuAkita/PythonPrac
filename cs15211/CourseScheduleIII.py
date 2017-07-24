__source__ = 'https://leetcode.com/problems/course-schedule-iii/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 630. Course Schedule III
#
# There are n different online courses numbered from 1 to n.
# Each course has some duration(course length) t and closed on dth day.
# A course should be taken continuously for t days and must be finished before or on the dth day.
# You will start at the 1st day.
#
# Given n online courses represented by pairs (t,d), your task is to find the maximal number of courses that can be taken.
#
# Example:
# Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
# Output: 3
# Explanation:
# There're totally 4 courses, but you can take 3 courses at most:
# First, take the 1st course, it costs 100 days so you will finish it on the 100th day,
# and ready to take the next course on the 101st day.
# Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day,
# and ready to take the next course on the 1101st day.
# Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.
# The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
# Note:
# The integer 1 <= d, t, n <= 10,000.
# You can't take two courses simultaneously.
#
# Companies
# WAP
# Related Topics
# Greedy
# Similar Questions
# Course Schedule Course Schedule II

# 635ms
import unittest
import heapq
class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        pq = []
        start = 0
        for t, end in sorted(courses, key = lambda (t, end): end):
            start += t
            heapq.heappush(pq, -t)
            while start > end:
                start += heapq.heappop(pq)
        return len(pq)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/course-schedule-iii/solution/

#72.98% 157ms
public class Solution {
    public int scheduleCourse(int[][] courses) {
        Arrays.sort(courses, (a, b) -> a[1] - b[1]);
        int max = 0;
        int time = 0;
        int count = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<int[]>((a, b) -> b[0] - a[0]);
        for(int i = 0; i < courses.length; i++){
            if(courses[i][0] + time <= courses[i][1]){
                time += courses[i][0];
                pq.add(courses[i]);
                count++;
            }
            else{
                if(pq.peek()[0] > courses[i][0]){
                    time -= pq.remove()[0];
                    time += courses[i][0];
                    pq.add(courses[i]);
                }
            }

        }

        return count;
    }
}

#98.49%  88ms // without using lambda
public class Solution {
    public int scheduleCourse(int[][] courses) {
        Arrays.sort(courses, new Comparator<int[]>(){
           public int compare(int[] a, int[] b){
               return a[1] - b[1];
           }
        });
        int max = 0;
        int time = 0;
        int count = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<int[]>(new Comparator<int[]>(){
            public int compare(int[] a, int[] b){
                return b[0] - a[0];
            }
        });
        for(int i = 0; i < courses.length; i++){
            if(courses[i][0]+time <= courses[i][1]){
                time+=courses[i][0];
                pq.add(courses[i]);
                count++;
            }
            else{
                if(pq.peek()[0] > courses[i][0]){
                    time -= pq.remove()[0];
                    time += courses[i][0];
                    pq.add(courses[i]);
                }
            }

        }

        return count;
    }
}


#56.81% 175ms
public class Solution {
    public int scheduleCourse(int[][] courses) {
        //Sort the courses by their deadlines (Greedy! We have to deal with courses with early deadlines first)
        Arrays.sort(courses, (a, b) -> a[1] - b[1]);
        //desc, start with course required the most hours to complete
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b) -> b - a);
        int time = 0;
        for (int[] course : courses) {
            time += course[0]; // estimated compelte time
            pq.add(course[0]);
            if (time > course[1]) { //If time exceeds, drop the previous course which costs the most time.
                time -= pq.poll();
            }
        }
        return pq.size();
    }
}

'''