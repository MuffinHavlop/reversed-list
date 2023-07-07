list = [3, 6, 1, 2, 7 ,8 ,9]
reversed_list = []

for i in range(1, len(list)):
    j = -i
    reversed_list.append([list[j]])

reversed_list.append([list[0]])

print(reversed_list)