class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        dup = {}

        for i, num in enumerate(nums):
            if num in dup and i-dup[num] <= k:
                return True
            dup[num] = i

        return False
