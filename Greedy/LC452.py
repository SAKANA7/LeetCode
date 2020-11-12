# @lc app=leetcode.cn id=452 lang=python
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        size = len(points)
        if size < 2:
            return size
        points.sort(key = lambda x : x[0])
        ans = 1
        end = points[0][1]
        for i in range(1, size):
            if  points[i][0] > end:
                ans  += 1
                end = points[i][1]
            else:
                end = min(points[i][1], end)
        return ans
# @lc code=end