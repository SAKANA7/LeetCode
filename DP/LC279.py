# @lc app=leetcode.cn id=279 lang=python
class Solution:
    def numSquares(self, n: int) -> int:
        squareNums = []
        tmp = 1
        while (tmp * tmp) <= n:
            squareNums.append(tmp * tmp)
            tmp += 1
        length = len(squareNums)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for num in squareNums:
            for x in range(num, n + 1):
                dp[x] = min(dp[x], dp[x - num] + 1)
        if dp[n] != float('inf'):
            return dp[n]
        return -1
# @lc code=end