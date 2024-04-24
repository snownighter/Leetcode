class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:

        sum_count = defaultdict(int)
        count = 0
        
        # Calculate the sum and its occurrence for A and B
        for a in A:
            for b in B:
                sum_count[a + b] += 1
        
        # Check the negative sum in C and D
        for c in C:
            for d in D:
                if - (c + d) in sum_count:
                    count += sum_count[-(c + d)]
        
        return count
