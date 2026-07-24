# # Uing replace function
# class Solution:
#     def defangIPaddr(self, address: str) -> str:
#         return address.replace(".", "[.]")


# without replace function using loop
address = "1.1.1.1"
ans = " "
for i in address:
    if i != ".":
        ans += i

    else:
        ans += "[.]"

print(ans)
