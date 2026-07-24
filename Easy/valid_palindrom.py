# First method to check if an string is palindrom using builtin isalnum() method
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            elif s[i].lower() != s[j].lower():
                return False
            else:
                i, j = i + 1, j - 1
        return True


s = "A man, a plan, a canal: Panama"
obj = Solution()
print(obj.isPalindrome(s))


# Check if an string is palindrom 2nd method
class Solution:
    def isAlphanumeric(self, s):
        x = ord(s)
        if 65 <= x <= 90 or 97 <= x <= 122 or 48 <= x <= 57:
            return True
        return False

    def isPalindrome(self, s: str) -> bool:
        str = s.lower()
        i = 0
        j = len(str)-1

        while i < j:
            if not self.isAlphanumeric(str[i]):
                i += 1
            elif not self.isAlphanumeric(str[j]):
                j -= 1
            elif str[i] == str[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
