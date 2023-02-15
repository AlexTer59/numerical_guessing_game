import random


# Проверка правильности введенного числа
def is_valid(val_num, start, end):
    while not (is_number(val_num) and start <= int(val_num) <= end):
        print("А может быть все-таки введем целое число от", start, "до", end)
        val_num = input()
        continue
    return int(val_num)


# Проверка равенства рандомного и введенного числа
def is_true_num(rand_num, true_num, start, end):
    attempts = 1
    while true_num != rand_num:
        if true_num < rand_num:
            print("Ваше число меньше загаданного, попробуйте еще разок...")
            attempts += 1
            true_num = input()
            true_num = is_valid(true_num, start, end)
            continue
        elif true_num > rand_num:
            print("Ваше число больше загаданного, попробуйте еще разок...")
            attempts += 1
            true_num = input()
            true_num = is_valid(true_num, start, end)
            continue
    print("Вы угадали, поздравляем!")
    print("Чтобы угадать Вам потребовалось", attempts, "попыток.")


# Обработка ответа пользователя
def is_restart(restart_answer):
    if restart_answer == 'y' or restart_answer == 'n':
        if restart_answer == 'n':
            global play_again
            play_again = False
    else:
        print("А может быть все-таки введем Y или N:")
        restart_answer = input()
        is_restart(restart_answer)


# Обработка корректности ввода диапазона
def is_valid_range(start, end):
    while not (is_number(start) and is_number(end) and int(start) < int(end)):
        print("А может быть все-таки введем корректный диапазон?")
        print("A = ", end='')
        start = input()
        print("B = ", end='')
        end = input()
        continue
    return int(start), int(end)


# Проверка если вводимые числа являются отрицательными
def is_number(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


# Главная программа
play_again = True
print("Добро пожаловать в числовую угадайку!")
while play_again:
    print("Введите диапазон загадываемого числа от A до B:")
    print("A = ", end='')
    a = input()
    print("B = ", end='')
    b = input()
    a, b = is_valid_range(a, b)
    rand_num = random.randint(a, b)
    print("Введите число в диапазоне от", a, "до", b)
    input_num = input()
    input_num = is_valid(input_num, a, b)
    is_true_num(rand_num, input_num, a, b)
    print("Сыграем еще раз Y/N?")
    answer = input().lower()
    is_restart(answer)
print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
