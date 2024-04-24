class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:

        # nums = sorted(nums)

        output = 0
        
        for last in range(3, len(nums)): 
            for left in range(0, last-2):
                for right in range(left+2, last):
                    i = left + 1
                    outside = nums[last] - (nums[left] + nums[right])
                    # print(left, i, right)
                    while i < right:
                        inside = nums[i]
                        if inside == outside:
                            output += 1
                            # print(nums[left], nums[i], nums[right], nums[last])
                        i += 1

        return output
