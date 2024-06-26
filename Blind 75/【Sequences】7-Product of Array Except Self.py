class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1]*n

        left, right = 1, 1
        # [1 1 1] output
        # [1 2 3] nums
        for i in range(n):
            output[i] *= left
            left *= nums[i]
        for i in range(n-1, -1, -1):
            output[i] *= right
            right *= nums[i]
        return output
