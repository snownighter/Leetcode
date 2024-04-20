class Solution:
    def countSubstrings(self, s: str) -> int:

        n = len(s)
        res = 0

        for size in range(1, n+1):
            num = n - size + 1
            for i in range(num):
                sub = s[i:i+size]
                if sub == sub[::-1]:
                    res += 1

        return res
        
    '''

    def countSubstrings(self, s: str) -> int:

        count = 0
        
        for i in range(len(s)):
            # 單個字符作為中心
            count += self.extend_palindrome(s, i, i)
            # 兩個相同字符作為中心
            count += self.extend_palindrome(s, i, i + 1)
        
        return count
    
    # 中心擴展，計算以 left 和 right 為中心的回文子串數量
    def extend_palindrome(self, s: str, left: int, right: int) -> int:
        count = 0
        # 從中心向兩側擴展，直到不是回文串為止
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count

    '''
