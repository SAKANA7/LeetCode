# @lc app=leetcode.cn id=860 lang=python
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        re5 = 0
        re10 = 0
        for i in bills:
            if i == 5:
                re5 += 1
            elif i == 10:
                if re5 < 1:
                    return False
                else:
                    re5 -= 1
                    re10 += 1
            elif i == 20:
                if re5 < 1:
                    return False
                else:
                    if re10 >= 1:
                        re10 -= 1
                        re5 -= 1
                    else:
                        if re5 < 3:
                            return False
                        else:
                            re5 -= 3
        return True
# @lc code=end