n = int(input('Введите число от 3 до 20: '))
variable = 20
result = []
for i in range(1,21):
    if i>=variable:
        break
    for j in range(i+1,n):
        if n % (i+j) == 0:
            result.append(i)
            result.append(j)
            variable = j
print('Пароль:',*result, sep='')