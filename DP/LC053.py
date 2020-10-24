# @lc app=leetcode.cn id=053 lang=python
class Solution:
    # 这是一个一维的动态。转移方程dp[i] = max(dp[i-1]+nums[i],nums[i]);，也比较好理解，
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        for i in range(1,n):
            if nums[i-1]>=0:
                nums[i]+=nums[i-1]
        return max(nums)
# @lc code=end