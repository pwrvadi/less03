# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def dev(*args):
    try:
        arg1 = int(input("Введите первое число "))
        arg2 = int(input("Введите второе число "))
        result = arg1 / arg2
    except ValueError:
        return 'Ошибка ввода'
    except ZeroDivisionError:
        return "Делить на ноль нельзя. Попробуйте снова"

    return result

    if arg2 == 0:
        print('Делить на ноль нельзя. Попробуйте снова')
    else:
        return arg1 / arg2


print(f'result  {dev()}')
