# # Uing replace function
# class Solution:
#     def defangIPaddr(self, address: str) -> str:
#         return address.replace(".", "[.]")


# # without replace function using loop
# address = "1.1.1.1"
# ans = " "
# for i in address:
#     if i != ".":
#         ans += i

#     else:
#         ans += "[.]"

# print(ans)


val_pal = "1223"
# reverse = ''.join(reversed(val_pal))
# if val_pal == reverse:
#     print("p")
# else:
#     print("n")

# print(val_pal)
# print(reverse)


def alphanumeric(s):
    x = ord(s)
    if 65 <= x <= 90 or 97 <= x <= 122 or 48 <= x <= 57:
        return True
    else:
        return False


s = val_pal.lower()
i = 0
j = len(val_pal)

while i < j:
    if not alphanumeric(s[i]):
        i += 1
    elif not alphanumeric(s[j]):
        j -= 1
    elif s[i] == s[j]:
        i += 1
        j -= 1
    else:
        print("false")
