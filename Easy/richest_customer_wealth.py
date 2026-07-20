
accounts = [[3, 5, 6, 2, 7], [1, 9, 4, 8, 3], [3, 10, 7, 10]]
ans = 0
for account in accounts:
    ans = max(ans, sum(account))


print(ans)
