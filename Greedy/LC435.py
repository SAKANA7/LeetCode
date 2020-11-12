# @lc app=leetcode.cn id=435 lang=python
# https://leetcode-cn.com/problems/non-overlapping-intervals/solution/tan-xin-suan-fa-zhi-qu-jian-diao-du-wen-ti-by-labu/
'''
一天有好多活动，你可以选择不重叠的时间参加多个活动。
按照活动结束的时间排序后（不管开始得多早，都不如选择早点结束的活动，这样还能继续选其他活动）
假设当前参加的是活动A，如果活动B的开始时间大于等于活动A的结束时间，则继续参加B活动。
这时活动数+1，后面的活动开始时间要和活动B结束的时间进行比较，所以活动结束的时间更新为活动B结束的时间。
'''
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        size = len(intervals)
        if size < 2:
            return 0
        intervals.sort(key = lambda x : x[1])
        end = intervals[0][1]
        cnt = 0
        for i in range(1, size):
            if intervals[i][0] < end:
                cnt += 1
            else:
                end = intervals[i][1]
        return cnt
# @lc code=end