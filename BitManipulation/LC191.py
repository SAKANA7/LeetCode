# @lc app=leetcode.cn id=191 lang=python
class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        解法1：
        这个就是移位计数
        ans = 0
        while n:
            ans += n & 1
            n >>= 1
        return ans
        '''
        '''
        解法2：
        这个是说bin()把数字变成二进制，然后计算二进制里面有几个'1'
        return bin(n).count('1')
        '''
        '''
        解法3：
        二进制中最低位的1会通过n-1操作消失，而比最低位1高的位不变，通过n&=n-1保留剩余高位的1及低位的0；
        示例：n=12，其二进制为1100，n-1为1011，n&(n-1)为1000，消掉了最低位的1
        时间复杂度：O(1)，n为32位的数，操作次数为二进制中1的个数
        '''
        ans=0
        while n:
            n&=n-1
            ans+=1
        return ans

# @lc code=end
