# Задача "А как делить?": (для module_4_1)

# В fake_math создайте функцию divide, которая принимает два параметра first и second.
# Функция должна возвращать результат деления first на second, но когда в second записан 0 - возвращать строку 'Ошибка'.

def divide(first, second):
    if second == 0:
        result = 'Ошибка'
    else:
        result = first / second
    return result