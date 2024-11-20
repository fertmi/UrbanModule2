first = int(input('Введите первое целое число:'))
second = int(input('Введите второе целое число:'))
third = int(input('Введите третье целое число:'))
number_of_digits = 'Количество одинаковых чисел:'
if first==second and second==third:
    print (number_of_digits,'3')
elif first==second or second==third or first==third:
    print (number_of_digits,'2')
else: print (number_of_digits,'0')