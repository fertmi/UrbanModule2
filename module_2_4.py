#It's not that simple.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True
for i in range(len(numbers)): # цикл для перебора списка
    if numbers[i] == 1:       # если 1, то пропустить
        continue
    for j in range(2,numbers[i]): # цикл для проверки деления на число от 2 до числа из списка
        if numbers[i] % j == 0:   # проверка деления без остатка
            is_prime = False      # если делится, то это непростое число
            break                 # прервать процесс деления
        else:
            is_prime = True       # простое число, если после перебора циклом не делится без остатка
    if is_prime == True:
        primes.append(numbers[i])      # если простое число, добавляем в список простых чисел
    else:
        not_primes.append(numbers[i])  # если число непростое, добавляем в список непростых чисел
print('Простые числа: ', primes)
print('Непростые числа: ', not_primes)