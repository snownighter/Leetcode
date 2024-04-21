class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        # 定義計數器
        t_counter = Counter(t)
        s_counter = Counter()
        
        left, right = 0, 0
        min_len = float('inf')
        min_window = ""
        
        while right < len(s):
            # 右邊界向右移動，更新計數器
            s_counter[s[right]] += 1
            right += 1
            
            # 當窗口包含了字符串 t 中的所有字符時，縮小窗口大小
            while all(s_counter[char] >= t_counter[char] for char in t_counter):
                # 更新最小子串的位置和長度
                if right - left < min_len:
                    min_len = right - left
                    min_window = s[left:right]
                
                # 左邊界向右移動，更新計數器
                s_counter[s[left]] -= 1
                left += 1

                # print(left)

            # print("##", left, right, min_window)
        
        return min_window
