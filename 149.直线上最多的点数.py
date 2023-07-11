#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#

# @lc code=start
import math
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # 暴力法
        # 两点确定一条直线，遍历所有的点，看看有多少个点在这条直线上
        # 但是这样的话，会有一个问题，就是斜率的表示，因为斜率是一个浮点数，所以不能直接用斜率来表示
        # 但是可以用最简分数来表示斜率，这样就可以用一个字典来表示斜率了
        # 但是这样的话，还有一个问题，就是斜率可能是无穷大，所以还要单独考虑，在代码中，用一个元组来表示
        # 还有一个问题，就是斜率可能是0，所以还要单独考虑
        # 还有一个问题，就是有可能有重复的点，所以还要单独考虑

        def gcd(a, b):
            if b == 0:
                return a
            else:
                return gcd(b, a % b)

        n = len(points)
        if n <= 2:
            return n
        res = 0
        for i in range(n):
            xielv = {}
            same = 0
            for j in range(i + 1, n):
                if points[i][0] == points[j][0] and points[i][1] == points[j][1]:
                    same += 1
                    continue
                x_delta = points[j][0] - points[i][0]
                y_delta = points[j][1] - points[i][1]
                #斜率无穷和斜率为0的情况，gcd都等于1
                g = gcd(x_delta, y_delta)

                x_delta //= g
                y_delta //= g

                k = (y_delta, x_delta)
                xielv[k] = xielv.get(k, 0) + 1

            if xielv:
                res = max(res, max(xielv.values()) + same + 1)
            else:
                res = max(res, same + 1)
        return res


# @lc code=end

