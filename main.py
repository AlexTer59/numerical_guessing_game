import random


# Проверка правильности введенного числа
def is_valid(val_num):
    while not (val_num.isdigit() and 1 <= int(val_num) <= 100):
        print("А может быть все-таки введем целое число от 1 до 100?")
        val_num = input()
        continue
    return int(val_num)


# Проверка равенства рандомного и введенного числа
def is_true_num(rand_num, true_num):
    while true_num != rand_num:
        if true_num < rand_num:
            print("Ваше число меньше загаданного, попробуйте еще разок...")
            global attempts
            attempts += 1
            true_num = input()
            true_num = is_valid(true_num)
            continue
        elif true_num > rand_num:
            print("Ваше число больше загаданного, попробуйте еще разок...")
            global attempts
            attempts += 1
            true_num = input()
            true_num = is_valid(true_num)
            continue
    print("Вы угадали, поздравляем!")


# Главная прграмма

attempts = 1
print("Добро пожаловать в числовую угадайку!")
print("Введите число от 1 до 100:")
rand_num = random.randint(1, 100)
input_num = input()
input_num = is_valid(input_num)
is_true_num(rand_num, input_num)
print("Спасибо, что играли в числовую угадайку. Еще увидимся...")

