#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start


from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #双哈希表+滑动窗口（双指针）
        #t_hash用于统计t中每个字符出现的次数
        #windows_hash用于统计滑动窗口中每个字符出现的次数
        #设定两个指针，left和right，分别指向滑动窗口的左右边界
        #right指针先移动，直到滑动窗口中包含了t中的所有字符，需要用一个变量valid来记录滑动窗口中满足条件的字符个数
        #过程是当右边字符在t_hash中出现时，windows_hash中对应字符的出现次数+1，当windows_hash中对应字符的出现次数等于t_hash中对应字符的出现次数时，valid+1
        #当valid等于t_hash的长度时，说明滑动窗口中包含了t中的所有字符
        #此时开始向右移动左指针，循环条件是valid等于t_hash的长度且left<=right
        #更新最小覆盖子串的长度和起始位置，更新windows_hash对应左指针字符的出现次数
        #当左边字符在t_hash中，且windows_hash中对应字符的出现次数小于t_hash中对应字符的出现次数时，valid-1
        #循环体内，left指针向右移动一位，直到valid不等于t_hash的长度或者left>right
        #最后返回最小覆盖子串的起始位置和长度
        t_hash = defaultdict(int)
        windows_hash = defaultdict(int)
        for i in t:
            t_hash[i] += 1
        left = 0
        right = 0
        valid = 0
        req = len(t_hash)
        ans = 0, 0
        length = float('inf')
        while right < len(s):
            #更新windows_hash
            c = s[right]
            windows_hash[c] += 1
            #更新valid
            if c in t_hash and windows_hash[c] == t_hash[c]:
                valid += 1
            #当valid等于req时，说明滑动窗口中包含了t中的所有字符,开始移动左指针
            while left <= right and valid==req:
                #更新最小覆盖子串的起始位置和长度
                if right - left + 1 < length:
                    ans = left, right
                    length = right - left + 1
                #更新windows_hash
                c = s[left]
                windows_hash[c] -= 1
                #更新valid
                if c in t_hash and windows_hash[c] < t_hash[c]:
                    valid -= 1
                #左指针向右移动一位
                left += 1
            #右指针向右移动一位
            right += 1
        return "" if length == float('inf') else s[ans[0]:ans[1]+1]
    

            

        
# @lc code=end

