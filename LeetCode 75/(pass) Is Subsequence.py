class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        n = 0
        for ts in t:
            if s[n] == ts:
                n += 1
                if n == len(s):
                    return True
        return False
