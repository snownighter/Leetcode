class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        count = {}

        for i, num in enumerate(numbers):
            n = target - num
            if n in count:
                return [count[n]+1, i+1]
            else:
                count[num] = i

        return []
        
