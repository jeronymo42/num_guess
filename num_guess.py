from random import randint as r
num = r(1, 100)

def is_valid():
    while True:
        n = input('Введи число =) \n')
        if n.isdigit() and 1 <= int(n) <= 100:
            return int(n)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            continue
print('Добро пожаловать в числовую угадайку')
while True:
    n = is_valid()
    if n > num:
        print('Слишком много, попробуйте еще раз')
        continue
    elif n < num:
        print('Слишком мало, попробуйте еще раз')
        continue
    else:
        print('Вы угадали, поздравляем!')
        ans = input('Хотите сыграть еще раз? ("д" / "н")')
        if ans == 'д':
            num = r(1, 100)
            continue
        else:
            break
