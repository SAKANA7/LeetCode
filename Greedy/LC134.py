# @lc app=leetcode.cn id=134 lang=python
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        题解：https://leetcode-cn.com/problems/gas-station/solution/shi-yong-tu-de-si-xiang-fen-xi-gai-wen-ti-by-cyayc/
        自己在下面评论有写出自己的理解，它这个图和代码不太一致，只需要记得minIndex是终点，
        用最简便的方法写出找到minIndex（即现在的代码）即可，虽然这是不太符合题意的。
        '''
        n = len(gas)
        des = 0
        spare = 0
        minspare = float('inf')
        for i in range(n):
            spare += gas[i] - cost[i]
            if spare < minspare:
                minspare = spare
                des = i
        if spare < 0:   return -1
        else:   return (des + 1) % n
# @lc code=end