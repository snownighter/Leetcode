class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        '''
        nums = sorted(nums)
        li = set()
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        li.add(tuple(sorted([nums[i], nums[j], nums[k]])))
        return [list(i) for i in li]
        '''
        nums.sort()
        result = []
        n = len(nums)
        
        # nums    = [-1,0,1,2,-1,-4]
        # sort() -> [-4,-1,-1,0,1,2]
        #             ^       ^ A B

        for i in range(n - 2):
            # 避免重複
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # A, B
            left, right = i + 1, n - 1
            # target = A' + B'
            target = -nums[i]
            while left < right:
                # total = A + B
                total = nums[left] + nums[right]
                # find A + B
                if total == target:
                    result.append([nums[i], nums[left], nums[right]])
                    # 避免重複 1
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 避免重複 2
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
        
        return result
