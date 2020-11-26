# @lc app=leetcode.cn id=098 lang=python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 用递归法
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            val = node.val
            if val <= lower or val >= upper:
                return False
            if not helper(node.left, lower, val):
                return False
            if not helper(node.right, val, upper):
                return False
            return True
        return helper(root)
'''
    # 用颜色遍历法进行迭代形式的中序遍历
        WHITE, GREY = 0, 1
        ans = []
        stk = [(WHITE, root)]
        while stk:
            color, cur = stk.pop()
            if not cur:
                continue
            if color == WHITE:
                stk.append((WHITE, cur.right))
                stk.append((GREY, cur))
                stk.append((WHITE, cur.left))
            else:
                ans.append(cur.val)
        for i in range(1, len(ans)):
            if ans[i - 1] >= ans[i]:
                return False
        return True
'''
# @lc code=end