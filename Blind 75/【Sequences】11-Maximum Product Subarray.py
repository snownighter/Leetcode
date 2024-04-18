class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        max_prod = min_prod = result = nums[0]
        
        # [2,3,-2,4]

        for i in range(1, len(nums)):
            num = nums[i]
            if num < 0:
                max_prod, min_prod = min_prod, max_prod
            
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)

            #print(max_prod, min_prod)
            
            # 更新結果
            result = max(result, max_prod)
        
        return result
