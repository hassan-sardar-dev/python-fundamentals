# level 2 excerse 4 remove the duplicates from the list

original_list = [3, 1, 3, 2, 1, 5]
unique_list = []

for item in original_list:
    if item not in unique_list:
        unique_list.append(item)

print(unique_list)
