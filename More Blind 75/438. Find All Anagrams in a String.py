class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        '''
        m, n = len(s), len(p)

        sorts = ''.join(sorted(p))
        res = []

        if m < n:
            return []

        for i in range(m-n+1):
            if ''.join(sorted(s[i:i+n])) == sorts:
                res.append(i)

        return res
        '''

        p_count = Counter(p)
        s_count = Counter()
        left, right = 0, 0
        matched = 0
        result = []
        
        while right < len(s):
            # 添加右边界字符到窗口，并更新计数器
            char_right = s[right]
            s_count[char_right] += 1
            right += 1
            
            # 如果窗口大小超过p的长度，移动左边界，并更新计数器
            if right - left > len(p):
                char_left = s[left]
                s_count[char_left] -= 1
                if s_count[char_left] == 0:
                    del s_count[char_left]
                left += 1
            
            # 检查窗口是否与p的字符出现次数相等
            if right - left == len(p):
                if s_count == p_count:
                    result.append(left)
        
        return result
