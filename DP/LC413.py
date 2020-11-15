# @lc app=leetcode.cn id=413 lang=python
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        # 空间优化
        # dp[i] 代表以A[i] 为结尾的等差数列
        ans = 0
        n = len(A)
        if n < 3:
            return 0
        dp = 0
        for i in range(2, n):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp += 1
                ans += dp
            else:
                dp = 0

        return ans
        '''
        # dp[i] 代表以A[i] 为结尾的等差数列
        ans = 0
        n = len(A)
        if n < 3:
            return 0
        dp = [0 for _ in range(n)]
        dp[0], dp[1] = 0, 0
        for i in range(2, n):
            if A[i] - A[i - 1] == A[i - 1] - A[i - 2]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 0
        for i in range(n):
            ans += dp[i]
        return ans
        '''
# @lc code=end