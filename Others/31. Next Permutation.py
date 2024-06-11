class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # Step 1: Find the pivot
        pivot = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break
        
        if pivot == -1:  # No pivot found, meaning the array is in descending order
            nums.reverse()
            return
        
        # Step 2: Find the successor
        for i in range(n-1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break
        
        # Step 3: Reverse the suffix
        nums[pivot + 1:] = reversed(nums[pivot + 1:])
