import bisect

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        tail = []

        for num in nums:

            # Find insertion position
            idx = bisect.bisect_left(tail, num)

            # If num is greater than all elements
            if idx == len(tail):
                tail.append(num)

            # Replace existing value
            else:
                tail[idx] = num

        return len(tail)