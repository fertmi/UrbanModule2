my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index_list = 0
length_list = len(my_list)
while index_list < length_list and my_list[index_list]>=0:
    if my_list[index_list] > 0:
        print('Положительное число из списка:',my_list[index_list])
    index_list += 1