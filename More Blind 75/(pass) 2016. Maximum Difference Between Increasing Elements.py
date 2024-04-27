class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        small, diff = nums[0], 0

        for num in nums[1:]:
            small, diff = min(small, num), max(diff, num - small)
        
        return diff if diff != 0 else -1
