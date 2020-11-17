# @lc app=leetcode.cn id=094 lang=python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        '''
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
        return ans
        '''
        ans = []
        stk = []
        cur = root
        while stk or cur:
            while cur:
                stk.append(cur)
                cur = cur.left
            cur = stk.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans

    '''
        ans = []
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            ans.append(cur.val)
            dfs(cur.right)
        dfs(root)
        return ans
    '''
    '''
        if not root:    return []
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)
    '''
# @lc code=end