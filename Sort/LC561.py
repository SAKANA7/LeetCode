# @lc app=leetcode.cn id=561 lang=python
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i, ans = 0, 0
        while i < len(nums):
            ans += nums[i]
            i += 2
        return ans
# @lc code=end