class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        
        n = len(nums)

        '''
        beauty = 0
        for i in range(1, n-1):
            if max(nums[:i]) < nums[i] < min(nums[i+1:]):
                beauty += 2
            elif nums[i-1] < nums[i] < nums[i+1]:
                beauty += 1
            
        return beauty
        '''

        left_max = [0] * n
        right_min = [0] * n
        
        # 预处理每个位置左侧的最大值
        left_max[0] = nums[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], nums[i])
        
        # 预处理每个位置右侧的最小值
        right_min[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            right_min[i] = min(right_min[i + 1], nums[i])
        
        beauty_sum = 0
        
        # 遍历数组，计算每个位置的美丽值并累加
        for i in range(1, n - 1):
            if left_max[i - 1] < nums[i] < right_min[i + 1]:
                beauty_sum += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                beauty_sum += 1
        
        return beauty_sum
