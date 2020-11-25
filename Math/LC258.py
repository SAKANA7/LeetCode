# @lc app=leetcode.cn id=258 lang=python
class Solution:
    def addDigits(self, num: int) -> int:
        '''
        if num < 10:    return num
        else:
            next1 = 0
            while num != 0:
                next1 = next1 + num % 10
                num = num // 10
            return self.addDigits(next1)
        '''
        if len(str(num)) == 1:   return num
        tmp = list(str(num))
        new_num = sum([int(i) for i in tmp])
        return self.addDigits(new_num)
# @lc code=end