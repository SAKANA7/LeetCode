# @lc app=leetcode.cn id=264 lang=python
# 后置题：LC264
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        else:
            while (num % 2) == 0:
                num /= 2
            while (num % 3) == 0:
                num /= 3
            while (num % 5) == 0:
                num /= 5
            return num == 1

# @lc code=end