# @lc app=leetcode.cn id=123 lang=python

'''
# dp的二维解法
# 0：初始态，1：买入第一次，2：卖出第一次，3：买入第二次，4：卖出第二次
# 这样起到了串联的效果
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        dp = [[0] * 5 for _ in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        dp[0][3] = -prices[0]
        dp[0][4] = 0
        for i in range(1, n):
            dp[i][0] = 0
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] + prices[i]) # 利润1
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] - prices[i])
            dp[i][4] = max(dp[i-1][4], dp[i-1][3] + prices[i]) # 利润2
            # 把四个状态串联，是本题关键所在
        return max(dp[-1][0],dp[-1][1],dp[-1][2],dp[-1][3],dp[-1][4])
'''

# 贪心算法
# 太巧妙了，甚至有些感动，结合121题的贪心解法理解
# 为什么可以这样，举个例子，[10,20,30,100,99]
# 按方法得出的结果时100-10 = 90，可不可能100后面出现一个小于100的数m（例子里面时99），
# 然后(20-10)+(m-30) > (100-10)，当然不可能！因为左边的式子实际上是(m-20)-(30-20)，再加上m<100，所以无法实现
# 这就是这种方法能成立的原理所在
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_1 = min_2 = float('inf')
        profit_1 = profit_2 = 0
        for i in prices:
            # 前两行代表了无论如何profit_1都能取到单次的最大值，也就是121的效果
            min_1 = min(min_1, i)
            profit_1 = max(profit_1, i - min_1)
            # 这里的处理太巧妙了，i-profit_1的目的是为了下一步i-min_2时可以加上profit_1的值
            min_2 = min(min_2, i - profit_1)
            profit_2 = max(profit_2, i - min_2)
        return profit_2
# @lc code=end
