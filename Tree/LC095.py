# @lc app=leetcode.cn id=095 lang=python
'''
https://leetcode-cn.com/problems/unique-binary-search-trees-ii/solution/zi-ding-xiang-xia-by-powcai/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:  return []
        def helper(begin, end):
            ans = []
            if begin > end:     ans.append(None)
            for val in range(begin, end + 1):
                for left in helper(begin, val - 1):
                    for right in helper(val + 1, end):
                        root = TreeNode(val)
                        root.left = left
                        root.right = right
                        ans.append(root)
            return ans
        return helper(1, n)
# @lc code=end