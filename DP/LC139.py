# @lc app=leetcode.cn id=139 lang=python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for i in range(len(s) + 1)]
        dp[0] = True

        for i in range(len(s)):
            if dp[i] == True:
                for j in range(i + 1, len(s) + 1):
                    if s[i:j] in wordDict:
                        dp[j] = True

        return dp[-1]
# @lc code=end