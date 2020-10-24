# @lc app=leetcode.cn id=152 lang=python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Fmin means the mininum product in an array's first I elements. So does the Fmax.
        n = len(nums)
        if n == 1:
            return nums[0]
        Fmin = [0 for _ in range(n)]
        Fmax = [0 for _ in range(n)]
        Fmin[0] = nums[0]
        Fmax[0] = nums[0]
        for i in range(n):
            Fmin[i] = min(nums[i], Fmin[i - 1] * nums[i], Fmax[i - 1] * nums[i])
            Fmax[i] = max(nums[i], Fmin[i - 1] * nums[i], Fmax[i - 1] * nums[i])
        return max(Fmax)
# @lc code=end
