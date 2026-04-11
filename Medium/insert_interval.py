from typing import List
class Solution: # re-use Leetcode-56's merge solution
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        return self.merge(intervals)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        for intv in sorted(intervals, key=lambda x: x[0]):
            if ans and ans[-1][1] >= intv[0]:
                ans[-1][1] = max(ans[-1][1], intv[1])
            else:
                ans.append(intv)
        return ans

intervals = [[1,3],[6,9]]
newInterval = [2,5]

obj = Solution()
print(obj.insert(intervals, newInterval))