matrix = [[2, 5, 8, 2], [3, 4, 1, 7], [4, 9, 1, 6]]
n = len(matrix)
m = len(matrix[0])
total = n*m
c = 0
ans = []

row_start = 0
row_end = n-1
col_start = 0
col_end = m-1

while c < total:
    # Row_start= col_start -> col_end
    for i in range(col_start, col_end+1):
        ans.append(matrix[row_start][i])
        c += 1
    row_start += 1

    if c == total:
        break

    # col_end = row_start -> row_end
    for i in range(row_start, row_end+1):
        ans.append(matrix[i][col_end])
        c += 1
    col_end -= 1

    if c == total:
        break

# Row_end = col_end -> col_start
    for i in range(col_end, col_start-1, -1):
        ans.append(matrix[row_end][i])
        c += 1
    row_end -= 1

    if c == total:
        break

# Col_start = row_end -> row_start
    for i in range(row_end, row_start-1, -1):
        ans.append(matrix[i][col_start])
        c += 1
    col_start += 1
print(ans)
