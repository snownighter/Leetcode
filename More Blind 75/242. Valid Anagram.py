class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        '''
        return sorted(s) == sorted(t)
        '''

        if len(s) != len(t):
            return False
        
        char_count = {}
        
        # 统计第一个字符串中每个字符的出现次数
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1
        
        # 遍历第二个字符串，检查每个字符是否在哈希表中出现，并更新出现次数
        for char in t:
            if char in char_count:
                char_count[char] -= 1
                if char_count[char] < 0:
                    return False
            else:
                return False
        
        # 检查是否所有字符的出现次数都为零
        for count in char_count.values():
            if count != 0:
                return False
        
        return True
