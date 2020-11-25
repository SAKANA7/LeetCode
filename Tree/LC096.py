# @lc app=leetcode.cn id=096 lang=python
'''
https://leetcode-cn.com/problems/unique-binary-search-trees/solution/bu-tong-de-er-cha-sou-suo-shu-by-leetcode-solution/
'''
class Solution:
    def numTrees(self, n: int) -> int:
        '''
        # solution2: math:C(n + 1) = 2(2n + 1)/(n + 2) * C(n)
        C = 1
        for i in range(0, n):
            C *= 2 * (2 * i + 1) / (i + 2)
        return int(C)

        '''
        G = [0 for _ in range(n + 1)]
        G[0], G[1] = 1, 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]
        return G[n]

        '''
        G[n] 代表长度为n的序列能构成的不同二叉搜索树的个数
        F(n, i) 代表以i为根节点， 序列长度为n的不同二叉搜索树个数
        F(n, i) = G[i - 1] *G[n - i] 
        G[n] = sum(F[n, i] for i in range(1， n + 1))
        '''
# @lc code=end