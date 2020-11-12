# @lc app=leetcode.cn id=455 lang=python
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        cnt = 0
        lflag = 0
        rflag = len(s)
        for i in g:
            for j in range(lflag, rflag):
                if i <= s[j]:
                    cnt += 1
                    lflag = j + 1
                    break
        return cnt
# @lc code=end