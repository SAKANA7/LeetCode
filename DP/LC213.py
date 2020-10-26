# @lc app=leetcode.cn id=213 lang=python
# 其实就是把环拆成两个队列，一个是从0到n-1，另一个是从1到n，然后返回两个结果最大的。
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return  nums[0]
        elif n == 2:
            return max(nums)
        elif n == 3:
            return max(nums)
        else:
            array1 = nums[:n - 1] # 不偷最后一个
            array2 = nums[1:]   # 不偷第一个
            m = len(array1)
            dp2 = array1[0]
            dp1 = max(array1[0], array1[1])
            for i in range(2, m):
                max1 = max(dp1, dp2 + array1[i])
                dp2 = dp1
                dp1 = max1
            dp2 = array2[0]
            dp1 = max(array2[0], array2[1])
            for i in range(2, m):
                max2 = max(dp1, dp2 + array2[i])
                dp2 = dp1
                dp1 = max2
            return max(max2, max1)
# @lc code=end
