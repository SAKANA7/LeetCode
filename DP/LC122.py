# @lc app=leetcode.cn id=123 lang=python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        profit_tmp = 0
        minp = float('inf')
        for i in prices:
            minp = min(minp, i)
            profit_tmp = i - minp
            if profit_tmp > 0:
                profit += profit_tmp
                profit_tmp = 0
                minp = i
        return profit
'''
如果我们在图表上绘制给定数组中的数字，我们将会得到：


如果我们分析图表，那么我们的兴趣点是连续的峰和谷。

用数学语言描述为：


关键是我们需要考虑到紧跟谷的每一个峰值以最大化利润。如果我们试图跳过其中一个峰值来获取更多利润，那么我们最终将失去其中一笔交易中获得的利润，从而导致总利润的降低。

例如，在上述情况下，如果我们跳过 peak_ipeak_i和valley_jvalley_j
​	
试图通过考虑差异较大的点以获取更多的利润，获得的净利润总是会小与包含它们而获得的净利润，因为 C 总是小于 A+B。


'''
# @lc code=end
