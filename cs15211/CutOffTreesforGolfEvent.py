__source__ = 'https://leetcode.com/problems/cut-off-trees-for-golf-event/description/'
# Time:  O()
# Space: O()
#
# Description: Leetcode # 675. Cut Off Trees for Golf Event
#
# You are asked to cut off trees in a forest for a golf event.
# The forest is represented as a non-negative 2D map, in this map:
#
# 0 represents the obstacle can't be reached.
# 1 represents the ground can be walked through.
# The place with number bigger than 1 represents a tree can be walked through,
# and this positive number represents the tree's height.
# You are asked to cut off all the trees in this forest in the order of tree's height - always
# cut off the tree with lowest height first. And after cutting,
# the original place has the tree will become a grass (value 1).
#
# You will start from the point (0, 0) and you should output the minimum steps you need to walk
# to cut off all the trees. If you can't cut off all the trees, output -1 in that situation.
#
# You are guaranteed that no two trees have the same height and there is at least one tree needs to be cut off.
#
# Example 1:
# Input:
# [
#  [1,2,3],
#  [0,0,4],
#  [7,6,5]
# ]
# Output: 6
# Example 2:
# Input:
# [
#  [1,2,3],
#  [0,0,0],
#  [7,6,5]
# ]
# Output: -1
# Example 3:
# Input:
# [
#  [2,3,4],
#  [0,0,5],
#  [8,7,6]
# ]
# Output: 6
# Explanation: You started from the point (0,0) and you can cut off the tree in (0,0) directly without walking.
# Hint: size of the given matrix will not exceed 50x50.
#
# Related Topics
# Breadth-first Search Amazon

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
# 33.67% 497ms
class Solution {
    static int[][] dir = {{0,1}, {0, -1}, {1, 0}, {-1, 0}};

    public int cutOffTree(List<List<Integer>> forest) {
        if (forest == null || forest.size() == 0) return 0;
        int m = forest.size(), n = forest.get(0).size();

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[2] - b[2]);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (forest.get(i).get(j) > 1) {
                    pq.add(new int[] {i, j, forest.get(i).get(j)});
                }
            }
        }

        int[] start = new int[2];
        int sum = 0;
        while (!pq.isEmpty()) {
            int[] tree = pq.poll();
            int step = minStep(forest, start, tree, m, n);

            if (step < 0) return -1;
            sum += step;

            start[0] = tree[0];
            start[1] = tree[1];
        }

        return sum;
    }

    private int minStep(List<List<Integer>> forest, int[] start, int[] tree, int m, int n) {
        int step = 0;
        boolean[][] visited = new boolean[m][n];
        Queue<int[]> queue = new LinkedList<>();
        queue.add(start);
        visited[start[0]][start[1]] = true;

        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int[] curr = queue.poll();
                if (curr[0] == tree[0] && curr[1] == tree[1]) return step;

                for (int[] d : dir) {
                    int nr = curr[0] + d[0];
                    int nc = curr[1] + d[1];
                    if (nr < 0 || nr >= m || nc < 0 || nc >= n
                        || forest.get(nr).get(nc) == 0 || visited[nr][nc]) continue;
                    queue.add(new int[] {nr, nc});
                    visited[nr][nc] = true;
                }
            }
            step++;
        }

        return -1;
    }
}

#99.78% 192ms
class Solution {
    void qsort(int l,int r, int[] x, int[] y, int[] num)
    {
        int i =l;
        int j =r;
        int mid = num[(l+r)/2];
        while (i<j)
        {
            while (num[i]<mid) i++;
            while (num[j]>mid) j--;
            if (i<=j)
            {
                int tmp;
                tmp = x[i];
                x[i] = x[j];
                x[j] = tmp;
                tmp = y[i];
                y[i] = y[j];
                y[j] = tmp;
                tmp = num[i];
                num[i] = num[j];
                num[j] = tmp;
                i++;
                j--;
            }
        }
        if (i<r) qsort(i,r,x,y,num);
        if (j>l) qsort(l,j,x,y,num);
    }
    public int cutOffTree(List<List<Integer>> forest) {

        int len = forest.size();
        for (int i = 0;i<forest.size();i++)
        {
            if (forest.get(i).size()>len)
                len = forest.get(i).size();
        }
        int[][] map = new int[len][len];
        int[][] check = new int[len][len];
        for (int i = 0;i<len;i++)
            for (int j = 0;j<len;j++)
                if (i<forest.size()&&j<forest.get(i).size())
                map[i][j] = forest.get(i).get(j);
                else map[i][j]  =0;
        if (map[0][0]==0) return -1;
        int[] x = new int[len*len];
        int[] y = new int[len*len];
        int[] queuex = new int[len*len];
        int[] queuey = new int[len*len];
        int[] num = new int[len*len];
        int mark = 0;
        for (int i = 0;i<len;i++)
            for (int j = 0;j<len;j++)
            if (map[i][j]!=0)
            {
                x[mark] = i;
                y[mark] = j;
                num[mark] = map[i][j];
                mark++;
            }
        qsort(0,mark-1,x,y,num);

        int nowx = 0;
        int nowy = 0;
        int ans = 0;
        for (int k = 0;k<mark;k++)
        {
            int endx = x[k];
            int endy = y[k];
            for (int i = 0;i<len;i++)
                for (int j = 0;j<len;j++)
                    check[i][j] = -1;
            check[nowx][nowy] = 0;
            queuex[0] = nowx;
            queuey[0] = nowy;

            int l = -1,r = 0;
            while (check[endx][endy]==-1&&l<r)
            {
                l++;
                int tmpx = queuex[l];
                int tmpy = queuey[l];
                int tmpstep = check[tmpx][tmpy];
                if (tmpx>0&&map[tmpx-1][tmpy]!=0&&check[tmpx-1][tmpy]==-1)
                {
                    r++;
                    queuex[r] = tmpx-1;
                    queuey[r] = tmpy;
                    check[tmpx-1][tmpy] = tmpstep+1;
                }
                if (tmpy>0&&map[tmpx][tmpy-1]!=0&&check[tmpx][tmpy-1]==-1)
                {
                    r++;
                    queuex[r] = tmpx;
                    queuey[r] = tmpy-1;
                    check[tmpx][tmpy-1] = tmpstep+1;
                }
                if (tmpx<len-1&&map[tmpx+1][tmpy]!=0&&check[tmpx+1][tmpy]==-1)
                {
                    r++;
                    queuex[r] = tmpx+1;
                    queuey[r] = tmpy;
                    check[tmpx+1][tmpy] = tmpstep+1;
                }
                if (tmpy<len-1&&map[tmpx][tmpy+1]!=0&&check[tmpx][tmpy+1]==-1)
                {
                    r++;
                    queuex[r] = tmpx;
                    queuey[r] = tmpy+1;
                    check[tmpx][tmpy+1] = tmpstep+1;
                }
            }
            ans+=check[endx][endy];
            if (check[endx][endy]==-1) return -1;
            nowx = x[k];
            nowy = y[k];
        }
        return ans;
    }
}
/*
[[1,2,3],[0,0,4],[7,6,5]]
[[0,0,0,3528,2256,9394,3153],[8740,1758,6319,3400,4502,7475,6812],[0,0,3079,6312,0,0,0],[6828,0,0,0,0,0,8145],[6964,4631,0,0,0,4811,0],[0,0,0,0,9734,4696,4246],[3413,8887,0,4766,0,0,0],[7739,0,0,2920,0,5321,2250],[3032,0,3015,0,3269,8582,0]]

*/
'''