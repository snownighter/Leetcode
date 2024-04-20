class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left, right = 0, 0
        max_length = 0
        
        # 跟蹤每個字符的最後出現位置
        char_index = {}
        
        while right < len(s):
            # 如果當前字符已經在表中，並且其最後出現位置在左指針右邊
            if s[right] in char_index and char_index[s[right]] >= left:
                # 收縮窗口
                left = char_index[s[right]] + 1
            
            # 更新當前字符的最後出現位置
            char_index[s[right]] = right
            
            # 更新最大長度
            max_length = max(max_length, right - left + 1)
            
            print(left, right, s[right], max_length, char_index)

            # 移動右指針
            right += 1
        
        return max_length
