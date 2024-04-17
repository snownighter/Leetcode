class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str in res:
                res[sorted_str].append(s)
            else:
                res[sorted_str] = [s]
        return list(res.values())
