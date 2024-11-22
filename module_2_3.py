my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index_list = 0
length_list = len(my_list) - 1
while index_list <= length_list:
    if my_list[index_list] > 0:
        print('Положительное число из списка:',my_list[index_list])
    elif my_list[index_list] < 0:
        break
    index_list = index_list + 1