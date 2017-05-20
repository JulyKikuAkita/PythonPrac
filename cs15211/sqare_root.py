__author__ = 'July'
# https://github.com/kamyu104/LeetCode/blob/master/Python/sqrtx.py
# Time:  O(logn)
# Space: O(1)
# Binary Search
#
# Implement int sqrt(int x).
#
# Compute and return the square root of x.
#

class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        if x < 2:
            return x

        low, high = 1, x /2
        while low <= high:
            mid = (low + high) / 2
            if x / mid < mid:
                high = mid - 1
            else:
                low = mid + 1
        return high


if __name__ == "__main__":
    print Solution().sqrt(10)
    print Solution().sqrt(6)

# y1= 1/2*(y0+x/y0)
class SolutionOther:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        y, ans, isNeg =0 ,1, False
        if x < 0:
            isNeg = True
        if x == 0:
            return 0
        while ans != y and x >0:
            y = ans
            ans = 1.0/2 *(y +x/y)
            #print y, ans
        return int(ans) if isNeg == False else int(ans * -1)


t1=SolutionOther()
#print t1.sqrt(9)
#print t1.sqrt(14)
#print t1.sqrt(0)
#print t1.sqrt(1)
#print t1.sqrt(-1)
#print t1.sqrt(-100)

#java
js = '''
public class Solution {
    public int mySqrt(int x) {
        if ( x < 2) return x;
        long start = 1;
        long end = x / 2;

        while ( start + 1 < end ){
            long mid = start + (end - start) / 2;
            if ( mid * mid == x) return (int)mid;
            else if(mid * mid < x){
                start = mid;
            }else{
                end = mid;
            }
        }

        if (end * end <= x) return (int)end;
        else{
            return (int)start;
        }

    }
}
'''