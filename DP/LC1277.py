# @lc app=leetcode.cn id=1277 lang=python
# 这个和221实际是一样的
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        row, column = len(matrix), len(matrix[0])
        dp = [[0] * column for _ in range(row)]
        ans = 0
        for i in range(row):
            for j in range(column):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    ans = ans + dp[i][j]
        return ans
# @lc code=end
