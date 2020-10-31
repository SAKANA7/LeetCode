# @lc app=leetcode.cn id=215 lang=python
from heapq import heappop, heappush
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 堆排序->优先队列算法
        heap = []
        ans = []
        for num in nums:
            heappush(heap, num)
        while len(heap) != 0:
            ans.append(heappop(heap))
        return ans[-k]
        '''
        # 冒泡排序 仅排k个:太慢了
        # 外层循环控制循环次数：k次，内层循环控制循环多少趟
        for i in range(k):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    tmp = nums[j]
                    nums[j] = nums[j + 1]
                    nums[j + 1] = tmp
        return nums[-k]
        '''
# @lc code=end