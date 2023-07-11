#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        #需要一个栈，用于判断消去，如果通过规则判断消去到字符串结束位置，栈内仍然有字符，说明无效，否认有效
        #匹配括号可消去，即(->),{->},[->]
        #栈空时，不能读取右半括号

        match_dict= {
            "(":")","[":"]","{":"}"
        }

        judge_stack = []

        for sym in s:
            #print(judge_stack)
            if not judge_stack:
                if sym in (")","]","}"):
                    return False
                else:
                    judge_stack.append(sym)
            else:
                if sym not in (")","]","}"):
                    judge_stack.append(sym)
                else:
                    if sym == match_dict[judge_stack[-1]]:
                        judge_stack.pop()
                    else:
                        return False
        
        if judge_stack:
            return False
        else:
            return True
# @lc code=end

