# @lc app=leetcode.cn id=316 lang=python
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ans = []
        seen = set()
        last_occurrence = {c:i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            if c not in seen:
                while ans and c < ans[-1] and i < last_occurrence[ans[-1]]:
                    seen.discard(ans.pop())
                seen.add(c)
                ans.append(c)
        return ''.join(ans)
'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = ['0']  # 放一个比字母都小的字符
        # 遍历字符串，，若不在，
        for i, c in enumerate(s):
            # 看元素在不在栈里，若不在
            if c not in stack:
                # 从栈顶元素开始比较，如果比栈顶元素小且s中还会再出现栈顶元素，则弹出栈顶元素
                while c < stack[-1] and stack[-1] in s[i + 1:]:
                    stack.pop()
                # 压入新元素
                stack.append(c)
        return ''.join(stack[1:])

'''
# @lc code=end