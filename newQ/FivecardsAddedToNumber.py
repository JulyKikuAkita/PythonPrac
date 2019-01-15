__source__ = ''
# five numbers, between 1 to 52, inclusive,
# is there a formula with add, minus, times that make the ttl number to 42
# ex: a*b+c*d-e = 42

class Solution1:
    # @param nums, a list of integer
    # @return True or False
    def canFiveCardsSumToTtl(self, nums, ttl):
        if not nums or len(nums) != 5:
            return False
        for n in nums: #assume no duplicate n
            if n < 1 or n > 52:
                return False

        visited = [False for _ in xrange(len(nums))]
        return self.dfs(nums, visited, 0, 0)


    def dfs(self, nums, visited, idx, cur):
        if idx == len(nums):
            if cur == 42:
                return True
            else:
                return False
        for i in xrange(len(nums)):
            if not visited[i]:
                visited[i] = True
                if self.dfs(nums, visited, idx + 1, cur + nums[i]) : return True
                if self.dfs(nums, visited, idx + 1, cur - nums[i]) : return True
                if self.dfs(nums, visited, idx + 1, cur * nums[i]) : return True
                visited[i] = False
        return False

# assume no limit of 5 numbers
class Solution2:
    # @param nums, a list of integer
    # @return True or False
    def canFiveCardsSumToTtl(self, nums, ttl):
        if not nums or len(nums) != 5:
            return False
        for n in nums: #assume no duplicate n
            if n < 1 or n > 52:
                return False
        all = (ttl + 1) * 2
        dp = [False for _ in xrange(all)]
        dp[0] = True

        INF = 0x7fffffff
        dp2 = [INF for _ in xrange(all)]
        dp2[0] = 0

        for i in xrange(len(dp)):
            if dp[i] != INF:
                for num in nums:
                    print i, num, dp2
                    if i + num < all:
                        dp2[i + num] = i + num
                    elif i - num < all and i - num > 0:
                        dp2[i - num] = i - num
                    elif i * num < all:
                        dp2[i * num] = i * num
        return dp2[ttl] == ttl

#test
ttl = 2
nums1 = [4,20,40,3,1]
nums2 = [50,48,49,52,51]
nums3 = [3,19,10,1,6]

#print Solution1().canFiveCardsSumToTtl(nums3, ttl)
print Solution2().canFiveCardsSumToTtl(nums3, ttl)

Java = '''
# Thought:

import java.util.ArrayList;
import java.util.List;


public class Card {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Card test=new Card();
		test.Card("29 3 3 12 52");
	}
	//9:50
	public void Card(String input){
		if(input==null||input.length()==0){
			System.out.println("NO");
			return;
		}

		String[] process=input.split(" ");
		if(process.length!=5){
			System.out.println("NO");
			return;
		}

		int[] nums=new int[5];

		for(int i=0;i<process.length;i++){
			nums[i]=Integer.parseInt(process[i]);
			if(nums[i]>52||nums[i]<1){
				System.out.println("NO");
				return;
			}
		}

		boolean [] visited=new boolean[5];
		if(helper(nums,visited,0, 0,new ArrayList())){
			System.out.println("YES");
		}else{
			System.out.println("NO");
		}
	}


	public boolean helper(int[] nums, boolean[] visited,int index, int sum, ArrayList item){
		//1,2,3 =1+helper(2,3)
		if(index==5){
			if(sum==42){
				System.out.println(item);
				return true;
			}else{
				return false;
			}
		}

		for(int i=0;i<nums.length;i++){
			if(visited[i]==false){
				visited[i]=true;
				item.add(nums[i]);
				if(helper(nums,visited, index+1,sum+nums[i],item)) return true;
				if(helper(nums,visited, index+1,sum-nums[i],item)) return true;
				if(helper(nums,visited, index+1,sum*nums[i],item)) return true;

				item.remove(item.size()-1);
				visited[i]=false;

			}
		}
		return false;
	}
}

'''