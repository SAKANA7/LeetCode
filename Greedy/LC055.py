# @lc app=leetcode.cn id=055 lang=python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        rflag = 0 #标记能到达的最远下标,当rflag >= n, return True
        for i in range(n):
            if  i <= rflag:
                rflag = max(rflag, i + nums[i])
                if rflag >= n - 1: # 只有rflag更新的时候这个判断才有意义，所以写到里面
                    return True
        return False
# @lc code=end