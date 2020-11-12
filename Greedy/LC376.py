# @lc app=leetcode.cn id=376 lang=python
'''
首先，可以证明最长摆动序列一定可以以原始数组的第一个数作为开始。
证明如下：若存在某个以第二个数为开始的摆动序列，这个摆动序列里的第二个数比第一个数大，
而原始数组的第一个数比第二个数（也就是摆动序列的第一个数）大，则以原始数组的第一个数作为开始能使摆动序列长度+1；
若摆动序列里的第二个数比第一个数大，而原始数组的第一个数比第二个数小，则选取原始数组的第一个数或者第二个数作为摆动序列的第一个数是等价的，
不减少摆动序列长度。对于摆动序列中第二个数比第一个数小的情况对称可证。
'''
# 贪心
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        prediff = nums[1] - nums[0]
        if prediff != 0:    count = 2
        else:   count = 1
        for i in range(2, n):
            diff = nums[i] - nums[i - 1]
            if (diff * prediff) <= 0 and diff != 0:
                count += 1
                prediff = diff
        return count
'''
# 二维动规 n^2
        n = len(nums)
        if n < 2:
            return n
        up = [0 for _ in range(n)]
        down = [0 for _ in range(n)]
        up[0], down[0] = 1, 1
        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j] + 1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j] + 1)
        return max(up[n - 1], down[n - 1], 1)
'''
'''
动规，时间空间都为on
        n = len(nums)
        if n < 2:
            return n
        up = [0 for _ in range(n)]
        down = [0 for _ in range(n)]
        up[0], down[0] = 1, 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up[i] = down[i - 1] + 1
                down[i] = down [i - 1]
            elif nums[i] < nums[i - 1]:
                down[i] = up[i - 1] + 1
                up[i] = up[i - 1]
            else:
                down[i] = down[i - 1]
                up[i] = up[i - 1]
        return max(down[n - 1], up[n - 1])
'''
'''
动规，时间on空间o1
        n = len(nums)
        if n < 2:
            return n
        up = 1
        down = 1
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                up = down + 1
            elif nums[i] < nums[i - 1]:
                down = up + 1
        return max(down, up)
'''
# @lc code=end