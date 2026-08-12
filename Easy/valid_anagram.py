from typing import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        cnt = Counter(s)
        for c in t:
            cnt[c] -= 1
            if cnt[c] < 0:
                return False
        return True


s = "anagram"
t = "nagaram"

obj = Solution()
print(obj.isAnagram(s, t))


# 2nd way

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}

        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        for i in t:
            if i not in freq:
                False
            else:
                freq[i] -= 1

        for i in freq.values():
            if i != 0:
                False
        return True
