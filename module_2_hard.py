n = int(input('Введите число от 3 до 20: '))
variable = 20
first_pair = 1
result = []
while first_pair<=variable:                    # цикл для первого числа пары
    for second_pair in range(first_pair+1,n):  # цикл для второго числа пары
        if n % (first_pair+second_pair) == 0:  # если заданное число делится без остатка на сумму пары
            result.append(first_pair)          # запись в список первого числа пары
            result.append(second_pair)         # запись в список второго числа пары
            variable = second_pair
    first_pair += 1
print('Пароль:',*result, sep='')