import bisect

__source__ = 'https://leetcode.com/problems/exam-room/'
# Time:  O(N)
# Space: O(N)
#
# Description: Leetcode # 855. Exam Room
#
# In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.
#
# When a student enters the room,
# they must sit in the seat that maximizes the distance to the closest person.
# If there are multiple such seats, they sit in the seat with the lowest number.
# (Also, if no one is in the room, then the student sits at seat number 0.)
#
# Return a class ExamRoom(int N) that exposes two functions:
# ExamRoom.seat() returning an int representing what seat the student sat in,
# and ExamRoom.leave(int p) representing that the student in seat number p now leaves the room.
# It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p.
#
# Example 1:
#
# Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
# Output: [null,0,9,4,2,null,5]
# Explanation:
# ExamRoom(10) -> null
# seat() -> 0, no one is in the room, then the student sits at seat number 0.
# seat() -> 9, the student sits at the last seat number 9.
# seat() -> 4, the student sits at the last seat number 4.
# seat() -> 2, the student sits at the last seat number 2.
# leave(4) -> null
# seat() -> 5, the student sits at the last seat number 5.
# Note:
#
# 1 <= N <= 10^9
# ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across all test cases.
# Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting in seat number p.
#
import unittest

#43.95% 224ms
class ExamRoom(object):
    def __init__(self, N):
        self.N = N
        self.students = []

    def seat(self):
        # Let's determine student, the position of the next
        # student to sit down.
        if not self.students:
            student = 0
        else:
            # Tenatively, dist is the distance to the closest student,
            # which is achieved by sitting in the position 'student'.
            # We start by considering the left-most seat.
            dist, student = self.students[0], 0
            for i, s in enumerate(self.students):
                if i:
                    prev = self.students[i-1]
                    # For each pair of adjacent students in positions (prev, s),
                    # d is the distance to the closest student;
                    # achieved at position prev + d.
                    d = (s - prev) / 2
                    if d > dist:
                        dist, student = d, prev + d

            # Considering the right-most seat.
            d = self.N - 1 - self.students[-1]
            if d > dist:
                student = self.N - 1

        # Add the student to our sorted list of positions.
        bisect.insort(self.students, student)
        return student

    def leave(self, p):
        self.students.remove(p)

class TestMethods(unittest.TestCase):
    def test_Local(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()

Java = '''
#Thought: https://leetcode.com/problems/exam-room/solution/
# Approach 1: Maintain Sorted Positions
# Complexity Analysis
# Time Complexity: Each seat operation is O(P), (where P is the number of students sitting),
# as we iterate through every student. Each leave operation is O(P) (logP in Java).
# Space Complexity: O(P), the space used to store the positions of each student sitting.
#
# TreeSet
# 108ms 39.37%
class ExamRoom {
    int N;
    TreeSet<Integer> students;

    public ExamRoom(int N) {
        this.N = N;
        students = new TreeSet();
    }

    public int seat() {
        int student = 0;
        if (students.size() > 0) {
            int dist = students.first();
            Integer prev = null;
            for (Integer s : students) {
                if (prev != null) {
                    int d = (s - prev) / 2;
                    if (d > dist) {
                        dist = d;
                        student = prev + d;
                    }
                }
                prev = s;
            }
            //Considering the right-most seat.
            if (N - 1 - students.last() > dist) student = N - 1;
        }
        students.add(student);
        return student;

    }

    public void leave(int p) {
        students.remove(p);
    }
}

# Thought:
https://leetcode.com/problems/exam-room/discuss/148595/Java-PriorityQueue-with-customized-object.-seat%3A-O(logn)-leave-O(n)-with-explanation

# PQ + interval, sort distance
# 68ms 99.05%
class ExamRoom {
    PriorityQueue<Interval> pq;
    int N;
    class Interval {
        int x, y, dist;

        public Interval(int x, int y) {
            this.x = x;
            this.y = y;
            if (x == -1) this.dist = y;
            else if (y == N) this.dist = N - 1 -x ;
            else this.dist = Math.abs( y - x) / 2;
        }
    }

    public ExamRoom(int N) {
        this.pq = new PriorityQueue<>((a,b) -> a.dist != b.dist? b.dist - a.dist : a.x - b.x); //why not b.x - a.x
        this.N = N;
        pq.add(new Interval(-1, N));
    }

    public int seat() {
        int seat = 0;
        Interval interval = pq.poll();
        if (interval.x == -1) seat = 0; // first student
        else if (interval.y == N) seat = N -1;
        else seat = (interval.x + interval.y) / 2;

        pq.offer(new Interval(interval.x, seat));
        pq.offer(new Interval(seat, interval.y));

        return seat;
    }

    public void leave(int p) {
        Interval head = null, tail = null;
        List<Interval> intervals = new ArrayList<>(pq);
        for (Interval interval : intervals) {
            if (interval.x == p) tail = interval;
            if (interval.y == p) head = interval;
            if (head != null && tail != null) break;
        }

        // Delete
        pq.remove(head);
        pq.remove(tail);
        // Merge
        pq.offer(new Interval(head.x, tail.y));
    }
}

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom obj = new ExamRoom(N);
 * int param_1 = obj.seat();
 * obj.leave(p);
 */
/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom obj = new ExamRoom(N);
 * int param_1 = obj.seat();
 * obj.leave(p);
 */

'''