# @lc app=leetcode.cn id=313 lang=python
'''
# 用丑数-II 的方法, TLE了
from heapq import heappop, heappush
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        nums = [] # 按顺序存储超级丑数
        seen = []
        heap = []
        heappush(heap, 1)
        for _ in range(n):
            curr_ugly = heappop(heap)
            # nums.append(curr_ugly)
            for i in primes:
                new_ugly = i * curr_ugly
                if new_ugly not in seen:
                    seen.append(new_ugly)
                    heappush(heap, new_ugly)
        return curr_ugly
'''
'''
# 结果发现, set add比append要快? 也挺神奇的。
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # nums = [] # 按顺序存储超级丑数
        seen = set()
        heap = []
        heappush(heap, 1)
        for _ in range(n):
            curr_ugly = heappop(heap)
            # nums.append(curr_ugly)
            for i in primes:
                new_ugly = i * curr_ugly
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heappush(heap, new_ugly)
        return curr_ugly
'''
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # 和丑数II的n指针一样，不过这个zip用的是很聪明
        # https://www.runoob.com/python/python-func-zip.html
        dp = [0] * n
        dp[0] = 1
        pointer = [0] * len(primes)
        for i in range(1, n):
            dp[i] = min(dp[x] * y for x, y in zip(pointer, primes) )
            for j in range(len(primes)):
                if dp[i] == primes[j] * dp[pointer[j]]:
                    pointer[j] += 1
        return dp[-1]
# @lc code=end