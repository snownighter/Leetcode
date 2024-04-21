class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        frequent = Counter(nums)
        res = []

        num = sorted(frequent.items(), key=lambda x:x[1])
        while k > 0:
            res.append(num[-k][0])
            k -= 1

        return res

        '''

        # 使用 Counter 統計元素出現的頻率
        counter = Counter(nums)
        
        # 使用最小堆來維護頻率最高的 k 個元素
        heap = []
        for num, freq in counter.items():
            # 將元素和頻率轉換為 (頻率, 元素) 的形式
            # 並將其插入最小堆中
            heapq.heappush(heap, (freq, num))
            # 如果堆的大小超過 k，則彈出堆頂元素
            if len(heap) > k:
                heapq.heappop(heap)
        
        # 從堆中彈出前 k 個元素，並返回它們的元素部分
        return [num for _, num in heap]

        '''
