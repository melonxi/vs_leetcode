#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits)==0:
            return []
        def DFS(index,string):
            if index == len(digits):
                ans.append(string)
                return
            for char in num_to_en_dict[digits[index]]:
                DFS(index+1,string+char)

        num_to_en_dict = {}
        num_to_en_dict["2"] = ["a","b","c"]
        num_to_en_dict["3"] = ["d","e","f"]
        num_to_en_dict["4"] = ["g","h","i"]
        num_to_en_dict["5"] = ["j","k","l"]
        num_to_en_dict["6"] = ["m","n","o"]
        num_to_en_dict["7"] = ["p","q","r","s"]
        num_to_en_dict["8"] = ["t","u","v"]
        num_to_en_dict["9"] = ["w","x","y","z"]

        ans = []
        DFS(0,"")
        return ans

        
# @lc code=end

