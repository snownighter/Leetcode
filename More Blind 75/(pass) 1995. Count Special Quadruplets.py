class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:

        # nums = sorted(nums)

        output = 0
        
        for last in range(3, len(nums)): 
            for left in range(0, last-2):
                for right in range(left+2, last):
                    outside = nums[last] - (nums[left] + nums[right])
                    output += nums[left + 1:right].count(outside)

        return output
