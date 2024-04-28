class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count1 = Counter(s1)
        count2 = Counter()

        n1, n2 = len(s1), len(s2)

        left = right = 0

        # s2 = "eidbaooo", n2 = len(s2)
        while right < n2:

            # [1]: s2[right] = 'e'
            count2[s2[right]] += 1
            right += 1

            # range(left, right+1) > len(s1) -> del s2[left]
            if right - left > n1:
                count2[s2[left]] -= 1
                if count2[s2[left]] == 0:
                    del count2[s2[left]]
                left += 1

            if right - left == n1:
                if count1 == count2:
                    return True

        return False
