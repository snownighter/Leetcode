class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = {}
        pairs = 0
        for num in nums:
            target = k - num
            # print("[r]", target)
            if target in counter and counter[target] > 0:
                pairs += 1
                counter[target] -= 1
            else:
                counter[num] = counter.get(num, 0) + 1
            # print(pairs, counter)
        return pairs
