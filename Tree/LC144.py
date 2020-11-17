# @lc app=leetcode.cn id=144 lang=python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
    '''
        颜色标记法：好处是前中后序模板一致，方便记忆
        坏处是直接迭代用栈相比，出入栈两次更耗时间
        https://leetcode-cn.com/problems/binary-tree-inorder-traversal/solution/yan-se-biao-ji-fa-yi-chong-tong-yong-qie-jian-ming/
        WHITE, GREY = 0, 1
        ans = []
        stk = [(WHITE, root)]
        while stk:
            color, cur = stk.pop()
            if not cur:
                continue
            if color == WHITE:
                stk.append((WHITE, cur.right))
                stk.append((WHITE, cur.left))
                stk.append((GREY, cur))
            else:
                ans.append(cur.val)
        return ans
    '''
        ans = []
        stk = []
        cur = root
        while cur or stk:
            # 根左根左根左...
            while cur:
                ans.append(cur.val)
                stk.append(cur)
                cur = cur.left
            # 左边没有了，弹出栈顶，cur = cur.right
            cur = stk.pop()
            cur = cur.right
        return ans
    '''
        ans = []
        def dfs(cur):
            if not cur:
                return
            ans.append(cur.val)
            dfs(cur.left)
            dfs(cur.right)
        dfs(root)
        return ans
    '''
    '''
        if not root:    return []
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
    '''
# @lc code=end