list1 = [1, 2, 3, 4, 5, 6]

n = len(list1)
start = 0

for i in range(n):
    if list1[i] % 2 == 0:
        temp = list1[i]
        list1[i] = list1[start]
        list1[start] = temp
        start += 1


print(list1)
