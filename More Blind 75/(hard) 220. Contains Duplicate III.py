from sortedcontainers import SortedSet

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        
        if valueDiff < 0:
            return False
        
        window = SortedSet()
        for i, num in enumerate(nums):
            if i > indexDiff:
                window.remove(nums[i - indexDiff - 1])
            index = window.bisect_left(num - valueDiff)
            # print(index, len(window))
            if index < len(window) and window[index] <= num + valueDiff:
                return True
            window.add(num)
        
        return False

        '''
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:]):
                if j == indexDiff:
                    break
                if abs(num1-num2) <= valueDiff:
                    print(i, i+j+1, num1, num2)
                    return True

        return False
        '''
