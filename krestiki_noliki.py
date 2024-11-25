def check_winner():
    char_win = '*'
    for i in range(3):
        if len(set(area[i])) == 1 and set(area[i])=='X':
            char_win='X'
            break
        if len(set(area[i])) == 1 and set(area[i])=='0':
            char_win='0'
            break
        if area[0][i]==area[1][i]==area[2][i]=='X':
            char_win = 'X'
            break
        if area[0][i]==area[1][i]==area[2][i]=='0':
            char_win = '0'
            break
    if area[0][0]==area[1][1]==area[2][2]=='X':
        char_win = 'X'
    if area[0][0]==area[1][1]==area[2][2]=='0':
        char_win = '0'
    return char_win

def draw_area():
    for i in area:
        print(*i)
    print()
area = [['*','*','*'],['*','*','*'],['*','*','*']]
print('Добро пожаловать в крестики-нолики')
print('__________________________________')
draw_area()
for turn in range(1,10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char = '0'
        print('Ходят нолики')
    else:
        turn_char = 'X'
        print('Ходят крестики')
    row = int(input('Введите номер строки (1,2,3) ')) - 1
    column = int(input('Введите номер столбца (1,2,3) ')) - 1
    if area[row][column] == '*':
        area[row][column] = turn_char
    else:
        print('Ячейка уже занята, вы пропускаете ход')
        draw_area()
        continue
    draw_area()
    if check_winner() == 'X':
        print('Победа крестиков')
        break
    if check_winner() == '0':
        print('Победа ноликов')
        break
    if check_winner() == '*' and turn == 9:
        print('Ничья')