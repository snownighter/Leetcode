class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:

        unique, res = [], []

        for s in words:
            sorts = ''.join(sorted(s))
            if not unique or sorts != unique[-1]:
                unique.append(sorts)
                res.append(s)

        return res
        
