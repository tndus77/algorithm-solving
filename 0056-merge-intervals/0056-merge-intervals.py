class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        pivot_start, pivot_end = intervals[0][0], intervals[0][1]
        total = []

        for i in range(1, len(intervals)):
            start, end = intervals[i]

            if start > pivot_end:
                total.append([pivot_start, pivot_end])
                pivot_start, pivot_end = start, end
            else:
                # 계속 비교할 수 있음
                # pivot_end < end: pivot_end = end
                if pivot_end < end:
                    pivot_end = end
        total.append([pivot_start, pivot_end])
        
        return total