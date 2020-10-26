# @lc app=leetcode.cn id=221 lang=python
'''
题解两则：
https://leetcode-cn.com/problems/maximal-square/solution/zui-da-zheng-fang-xing-by-leetcode-solution/
https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones/solution/tong-ji-quan-wei-1-de-zheng-fang-xing-zi-ju-zhen-2/
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        row, column = len(matrix), len(matrix[0])
        maxside = 0
        '''
        dp = [[0] * column for _ in range(row)]
        for i in range(row):
            for j in range(column):
                if matrix[i][j] == '1': # 这个 '1' 真是太离谱了
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    maxside = max(maxside, dp[i][j])
        return (maxside * maxside)
        '''
        # 空间优化，使用matrix 这个是dp的一个优点
        for i in range(row):
            for j in range(column):
                matrix[i][j] = int(matrix[i][j])
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        matrix[i][j] = 1
                    else:
                        matrix[i][j] = min(matrix[i - 1][j], matrix[i - 1][j - 1], matrix[i][j - 1]) + 1
                    maxside = max(maxside, matrix[i][j])
        return (maxside * maxside)
# @lc code=end
