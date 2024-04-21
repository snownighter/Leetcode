class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # 按照結束位置排序
        intervals.sort(key=lambda x: x[1])

        #print(intervals)
        #print(intervals[0][1])
        
        # 初始化結束位置和刪除的區間數量
        end = intervals[0][1]
        count = 1
        
        # 遍歷每個區間
        for i in range(1, len(intervals)):
            #print("## ", i, intervals[i][0], end)
            # 如果當前區間的開始位置在前一個區間的結束位置之後，則添加到答案中
            if intervals[i][0] >= end:
                #print(intervals[i][0], ">=", end)
                end = intervals[i][1]
                count += 1
        
        # 返回需要刪除的區間數量
        return len(intervals) - count
