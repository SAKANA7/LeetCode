# @lc app=leetcode.cn id=406 lang=python
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        if len(people) <= 1:
            return people
        else:
            # 对队列排序，先按h降序，再按k升序
            people.sort(key = lambda x: (-x[0], x[1]))
            output = []
            for p in people:
                output.insert(p[1], p)
            return output
# @lc code=end