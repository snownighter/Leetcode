class Solution:
    def search(self, nums: List[int], target: int) -> int:

        '''
        return -1 if nums.count(target) == 0 else nums.index(target)
        '''

        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # 判斷哪一半是有序的
            if nums[left] <= nums[mid]:
                # 左半邊是有序的
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # 右半邊是有序的
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
