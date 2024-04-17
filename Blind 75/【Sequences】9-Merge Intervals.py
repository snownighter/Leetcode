class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if not intervals:
            return []

        # 起始點排序
        intervals.sort(key=lambda x: x[0])

        # [[1,3],[2,6],[8,10],[15,18]]

        # [[1,3],[2,6] ...
        # [[1,6] ...]
        
        merged_intervals = [intervals[0]]
        
        for val in intervals[1:]:

            last = merged_intervals[-1]
            
            if val[0] <= last[1]:
                last[1] = max(last[1], val[1])
            else:
                merged_intervals.append(val)
        
        return merged_intervals
