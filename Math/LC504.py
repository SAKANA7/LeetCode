# @lc app=leetcode.cn id=504 lang=python
# 这题要注意的是：python对于负数来说是向下取整，避免麻烦直接把负数换成正数加负号的形式
# https://blog.csdn.net/u012626619/article/details/80671233
class Solution:
    def convertToBase7(self, num: int) -> str:
        '''
        if num == 0:
            return '0'
        elif num < 0:
            ans = ''
            num = abs(num)
            integer = num // 7
            while integer != 0:
                remainder = num % 7
                num = num // 7
                ans = (str(remainder)) + ans
                integer = num // 7
            remainder = num % 7
            num = num // 7
            ans = (str(remainder)) + ans
            ans = '-' + ans
        elif num > 0:
            ans = ''
            integer = num // 7
            while integer != 0:
                remainder = num % 7
                num = num // 7
                ans = (str(remainder)) + ans
                integer = num // 7
            remainder = num % 7
            num = num // 7
            ans = (str(remainder)) + ans
        return ans
        '''
        base7 = []
        if num < 0:
            flag = 1
            num = -num
        else:
            flag = 0
        while num >= 7:
            fig = str(num % 7)
            base7.append(fig)
            num = num // 7
        base7.append(str(num))
        if flag:
            base7.append('-')
        base7.reverse()
        return ''.join(base7)
# @lc code=end