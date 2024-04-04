class Solution:
    def reverseWords(self, s: str) -> str:
        # print(s.split())
        return ' '.join(s.split()[::-1])
