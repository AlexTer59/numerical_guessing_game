import random


# Проверка правильности введенного числа
def is_valid(input_num):
    if input_num.isdigit() and 1 <= int(input_num) <= 100:
        return True
    else:
        return False


# Проверка равенства рандомного и введенного числа
def is_true_num(rand_num, input_num):
    if rand_num > int(input_num):
        return -1
    elif rand_num < int(input_num):
        return -2
    else:
        return 1


# Главная прграмма
def main():
    print("Добро пожаловать в числовую угадайку")
    print("Введите число от 1 до 100")
    # rand_num = random.randint(1, 100)
    rand_num = 40
    input_num = input()
    while not is_valid(input_num):
        print("А может быть все-таки введем целое число от 1 до 100?")
        input_num = input()
        is_valid(input_num)
    input_num = int(input_num)
    while is_true_num(rand_num, input_num):
        if is_true_num(rand_num, input_num) == -1:
            print("Ваше число меньше загаданного, попробуйте еще разок")
            input_num = input()
            continue
        elif is_true_num(rand_num, input_num) == -2:
            print("Ваше число больше загаданного, попробуйте еще разок")
            input_num = input()
            continue
        elif is_true_num(rand_num, input_num) == 1:
            print("Вы угадали, поздравляем!")
            print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
            break



# Вызов главной программы
main()
