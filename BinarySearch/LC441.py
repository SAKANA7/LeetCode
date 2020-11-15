# @lc app=leetcode.cn id=441 lang=python
# 二分查找
# https://leetcode-cn.com/problems/arranging-coins/solution/pai-lie-er-fen-fa-by-zui-weng-jiu-xian/
# 二分查找的边界处理实在太难了，心累。
class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = left + (right - left) // 2
            value = ((mid + 1) * mid) // 2
            if value == n:  return mid
            elif value < n: left = mid + 1
            else:   right = mid - 1
        return right
'''
# 数值分析里的学过的牛顿迭代法
class Solution:
    def arrangeCoins(self, n: int) -> int:
        value = n
        while abs(value*(value+1)/2 - n) > 0.01:
            value = (value*value + n*2) / (value*2 + 1)
        return int(value)
'''
'''
class Solution:
    def arrangeCoins(self, n: int) -> int:
        cnt = 1
        if n == 0:
            return 0
        n -= cnt
        while n >= 0:
            cnt += 1
            n -= cnt
        return cnt - 1
'''
# @lc code=end