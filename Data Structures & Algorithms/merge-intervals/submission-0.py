class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # ok so we have a condition that we 
        # need to find all the non overlapping intervals 
        
        intervals.sort()
        out = [intervals[0]]

        # we need to check if the start of one is bigger than the
        # end of prev
        # so if the cur interval overlaps with the alst one, so start <= lastEnd
        # we merge with seeing whats bigger, end or lastEnd
        # else no overlap: we append the cur interval to output 
        for start, end in intervals:
            lastEnd = out[-1][1]
            if (start <= lastEnd):
                out[-1][1] = max(lastEnd, end)
            else:
                out.append([start, end])
        return out


