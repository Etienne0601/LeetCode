class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort the intervals in increasing order by the start time
        intervals.sort(key=lambda x: x[0])
        
        # initialize the last variable to be the earliest interval in the list
        last = intervals[0]
        
        # initialize output list
        output = []
        
        for i in range(1, len(intervals)):
            # if last has a conflict with the next interval,
            # then expand last to cover the next interval as well
            # else, append last to the output list and then last
            # will become the next interval
            if intervals[i][0] <= last[1]:
                last[1] = max(intervals[i][1], last[1])
            else:
                output.append(last)
                last = intervals[i]
        
        # after we examine the last interval, last will contain the
        # last (perhaps extended) interval we need to append to output
        output.append(last)
        
        return output
