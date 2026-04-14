class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        a, b = map(int, num1[:-1].split('+'))
        c, d = map(int, num2[:-1].split('+'))
        return f'{a * c - b * d}+{a * d + c * b}i'


num1 = "1+1i"
num2 = "1+1i"

obj = Solution()
print(obj.complexNumberMultiply(num1, num2))