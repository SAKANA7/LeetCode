# @lc app=leetcode.cn id=063 lang=python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 0 or n == 0: return 0
        dp = [[0] * n for _ in range(m)]
        flagr, flagc = 0, 0 # 标记list[0][i]与list[j][0]中是否有障碍，若有则后面的都有
        # 遍历obstacleGrid[0]
        for i in range(n):
            if flagc == 0:
                if obstacleGrid[0][i] == 0:
                    dp[0][i] = 1
                else:
                    dp[0][i] = 0
                    flagc = 1
            elif flagc == 1:
                dp[0][i] = 0
        for i in range(m):
            if flagr == 0:
                if obstacleGrid[i][0] == 0:
                    dp[i][0] = 1
                else:
                    dp[i][0] = 0
                    flagr = 1
            elif flagr == 1:
                dp[i][0] = 0
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
# @lc code=end
