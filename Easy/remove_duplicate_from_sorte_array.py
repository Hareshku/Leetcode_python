array = [2, 2, 3, 4, 4, 5, 5, 6, 7, 7]

n = len(array)

start = 0

for i in range(1, n):

    # find unique element
    if array[i] != array[start]:
        start += 1
        array[start] = array[i]

print(start+1)
