# First way to do this problem

from typing import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1


s = "leetcode"
obj = Solution()
print(obj.firstUniqChar(s))

# Second way


class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        return -1
