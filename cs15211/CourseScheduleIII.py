__source__ = 'https://leetcode.com/problems/course-schedule-iii/'
# Time:  O(nlog(n))
# Space: O(n)
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

import unittest
import heapq

# 400ms 57.69%
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
# Thought: https://leetcode.com/problems/course-schedule-iii/solution/

# Approach #1 Brute Force [Time Limit Exceeded]
# Algorithm
# The most naive solution will be to consider every possible permutation of the given courses
# Complexity Analysis
# Time complexity : O((n+1)!). A total of n! permutations are possible for the courses array of length n. 
# For every permutation, we scan over the n elements of the permutation 
# to find the number of courses that can be taken in each case.
# Space complexity : O(n). Each permutation needs nn space.

Approach #2 Using Recursion with memoization[Time Limit Exceeded]
Complexity Analysis
Time complexity : O(n * d). memomemo array of size n x d is filled once. 
Here, n refers to the number of courses in the given course array 
and d refers to the maximum value of the end day from all the end days in the courses array.
Space complexity : O(n * d). memomemo array of size n x d is used.
# MLE
class Solution {
    public int scheduleCourse(int[][] courses) {
        Arrays.sort(courses, (a, b) -> a[1] - b[1]);
         Integer[][] memo = new Integer[courses.length][courses[courses.length - 1][1] + 1];
        return schedule(courses, 0, 0, memo);
    }
    
    public int schedule(int[][] courses, int i, int time, Integer[][] memo) {
        if (i == courses.length) return 0;
        if (memo[i][time] != null) return memo[i][time];
        int taken = 0;
        if (time + courses[i][0] <= courses[i][1]) {
            taken = 1 + schedule(courses, i + 1, time + courses[i][0], memo);
        }
        int not_taken = schedule(courses, i + 1, time, memo);
        memo[i][time] = Math.max(taken, not_taken);
        return memo[i][time];
    }
}
Approach #3 Iterative Solution [Time Limit Exceeded]
Complexity Analysis
Time complexity : O(n^2). We iterate over the count array of size nn once. 
For every element currently considered, we could scan backwards till the first element, giving O(n^2) complexity. 
Sorting the count array takes O(nlog(n)) time for count array.
Space complexity : O(1). Constant extra space is used.
# 1349ms 0%
class Solution {
    public int scheduleCourse(int[][] courses) {
        Arrays.sort(courses, (a, b) -> a[1] - b[1]);
        int time = 0, count = 0;
        for (int i = 0; i < courses.length; i++) {
            if (time + courses[i][0] <= courses[i][1]) { 
                time += courses[i][0];
                count++;
            } else {
                int max_i = i;
                for (int j = 0; j < i; j++) {
                    if (courses[j][0] > courses[max_i][0]) max_i = j;
                }
                if (courses[max_i][0] > courses[i][0]) {
                    time += courses[i][0] - courses[max_i][0];
                }
                courses[max_i][0] = -1;
                
            }
        }
        return count;
    }
}
Approach #4 Optimized Iterative [Accepted]
Complexity Analysis
Time complexity : O(n * count). We iterate over a total of nn elements of the coursescourses array. 
For every element, we can traverse backwards upto atmost countcount(final value) number of elements.
Space complexity : O(1). Constant extra space is used.
# 401ms 4%
class Solution {
    public int scheduleCourse(int[][] courses) {
        Arrays.sort(courses, (a, b) -> a[1] - b[1]);
        int time = 0, count = 0;
        for (int i = 0; i < courses.length; i++) {
            if (time + courses[i][0] <= courses[i][1]) { 
                time += courses[i][0];
                courses[count++] = courses[i];
            } else {
                int max_i = i;
                for (int j = 0; j < count; j++) {
                    if (courses[j][0] > courses[max_i][0]) max_i = j;
                }
                if (courses[max_i][0] > courses[i][0]) {
                    time += courses[i][0] - courses[max_i][0];
                    courses[max_i] = courses[i];
                }
                
            }
        }
        return count;
    }
}
Approach #5 Using Extra List [Accepted]
Complexity Analysis
Time complexity : O(n * m). We iterate over a total of n elements of the courses array. 
For every element, we can traverse over atmost mm number of elements. 
Here, mm refers to the final length of the alid_list.
Space complexity : O(n). The valid_list can contain at most n courses.
# 639ms 1%
class Solution {
    public int scheduleCourse(int[][] courses) {
        Arrays.sort(courses, (a, b) -> a[1] - b[1]);
        List< Integer > valid_list = new ArrayList < > ();
        int time = 0;
        for (int[] c: courses) {
            if (time + c[0] <= c[1]) {
                valid_list.add(c[0]);
                time += c[0];
            } else {
                int max_i=0;
                for(int i=1; i < valid_list.size(); i++) {
                    if(valid_list.get(i) > valid_list.get(max_i))
                        max_i = i;
                }
                if (valid_list.size() > max_i && valid_list.get(max_i) > c[0]) {
                    time += c[0] - valid_list.get(max_i);
                    valid_list.set(max_i, c[0]);
                }
            }
        }
        return valid_list.size();
    }
}

Approach #6 Using Priority Queue [Accepted]
Complexity Analysis
Time complexity : O(nlog(n)). At most nn elements are added to the queue. 
Adding each element is followed by heapification, which takes O(log(n)) time.
Space complexity : O(n). The queuequeue containing the durations of the courses taken can have atmost nn elements
# 159ms 59% 
class Solution {
    public int scheduleCourse(int[][] courses) {
        Arrays.sort(courses, (a, b) -> a[1] - b[1]);
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> (b - a));
        int time = 0;
        for (int[] c: courses) {
            if (time + c[0] <= c[1]) {
                pq.offer(c[0]);
                time += c[0];
            } else if (!pq.isEmpty() && pq.peek() > c[0]){
                time += c[0] - pq.poll();
                pq.offer(c[0]);
            }
        }
        return pq.size();
    }
}

#72.98% 157ms
class Solution {
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
            } else{
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
class Solution {
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


# 110ms 62.62%
class Solution {
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
