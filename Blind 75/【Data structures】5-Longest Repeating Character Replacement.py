class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        '''
        chars = set(s)
        longest = 0

        for ch in chars:
            for i in range(len(s)):
                n, m = 0, k
                for j in range(i, len(s)):
                    if s[j] == ch:
                        n += 1
                        longest = max(longest, n)
                    else:
                        if m > 0:
                            m -= 1
                            n += 1
                            longest = max(longest, n)
                        else:
                            longest = max(longest, n)
                            break
        
        return longest
        '''

        left = 0
        max_length = 0
        max_count = 0
        count = {}
        
        for right in range(len(s)):
            # 更新當前字符的出現次數
            count[s[right]] = count.get(s[right], 0) + 1
            # 更新當前最頻繁出現的字符次數
            max_count = max(max_count, count[s[right]])
            
            # 如果當前窗口大小減去最頻繁出現的字符次數大於 k，則需要收縮窗口
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            
            # 更新最大窗口長度
            max_length = max(max_length, right - left + 1)
        
        return max_length
