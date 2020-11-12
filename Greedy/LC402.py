# @lc app=leetcode.cn id=408 lang=python
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        remain = len(num) - k
        for i in num:
            while k and stack and stack[-1] > i:
                stack.pop()
                k -= 1
            stack.append(i)
        return ''.join(stack[:remain]).lstrip('0') or '0'
# @lc code=end