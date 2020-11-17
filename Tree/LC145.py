# @lc app=leetcode.cn id=145 lang=python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        '''
        WHITE, GREY = 0, 1
        ans = []
        stk = [(WHITE, root)]
        while stk:
            color, cur = stk.pop()
            if not cur:
                continue
            if color == WHITE:
                stk.append((GREY, cur))
                stk.append((WHITE, cur.right))
                stk.append((WHITE, cur.left))
            else:
                ans.append(cur.val)
        return ans
        '''
        # 前序：根-左右，后续：左右-根，所以用前序的方法然后返回deverse即可
        # 所以记忆的时候就：理解了前序的然后，做后序的时候稍作修改再reverse
        ans = []
        stk = []
        cur = root
        while cur or stk:
            while cur:
                ans.append(cur.val)
                stk.append(cur)
                cur = cur.right
            cur = stk.pop()
            cur = cur.left
        return ans[::-1]
    '''
        ans = []
        def dfs(cur):
            if not cur:
                return
            dfs(cur.left)
            dfs(cur.right)
            ans.append(cur.val)
        dfs(root)
        return ans
    '''
    '''
        if not root:    return []
        return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val]
    '''
# @lc code=end