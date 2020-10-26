# @lc app=leetcode.cn id=198 lang=python
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if  n==0:
            return 0
        elif n==1:
            return nums[0]
        elif n==2:
            return max(nums[0],nums[1])
        else:
            dp2=nums[0] # dp[i-2]
            dp1=max(nums[0],nums[1]) # dp[i-1]
            for i in range(2,n):
                dp=max(dp2+nums[i],dp1) # dp[i]=max(dp[i-2]+nums[i], dp[i-1])
                dp2=dp1
                dp1=dp
            return dp
# @lc code=end
