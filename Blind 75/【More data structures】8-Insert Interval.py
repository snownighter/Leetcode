class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        merged = []
        i, n = 0, len(intervals)
        
        # 將與新間隔重疊的間隔合併成一個新的間隔
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1
        
        # 將與新間隔重疊的間隔合併成一個新的間隔
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # 將新的間隔加入到結果列表中
        merged.append(newInterval)
        
        # 添加剩餘的間隔
        while i < n:
            merged.append(intervals[i])
            i += 1
        
        return merged
