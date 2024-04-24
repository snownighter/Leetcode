class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums = sorted(nums)

        output = []
        
        for left in range(0, len(nums)-3):
            for right in range(left+3, len(nums)):
                l, r = left+1, right-1
                outside = target - (nums[left] + nums[right])
                # print(left, l, r, right)
                while l < r:
                    inside = nums[l] + nums[r]
                    num_l, num_r = nums[l], nums[r]
                    if inside == outside:
                        output.append([nums[left], nums[l], nums[r], nums[right]])
                        while nums[l] == num_l and l < r:
                            l += 1
                        while nums[r] == num_r and l < r:
                            r -= 1
                    elif inside < outside:
                        while nums[l] == num_l and l < r:
                            l += 1
                    else:
                        while nums[r] == num_r and l < r:
                            r -= 1

        return list(set(tuple(i) for i in output))

