import json
import random


def task_1(a: int, b: int):
    def task_1_2():
        for i in range(a):
            if int(input('Введите число: ')) == b:
                return 'вы угадали'
        return 'неудача'

    return task_1_2


def gaming(func):
    def wrapper(a: int, b: int):
        if not 0 < b < 100:
            b = random.randint(1, 100)
            print(b)
        if not 0 < a < 10:
            a = random.randint(1, 10)
            print(a)
        return func(a, b)

    return wrapper


@gaming
def task_2(a: int, b: int):
    for i in range(a):
        if int(input('Введите число: ')) == b:
            return True
    return False


"""Напишите декоратор, который сохраняет в json файл
параметры декорируемой функции и результат, который она
возвращает. При повторном вызове файл должен
расширяться, а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ
json словаря.
Для декорирования напишите функцию, которая может
принимать как позиционные, так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой
функции.
"""


def func_json(func):
    list_of_dict = []

    def wrapper(*args, **kwargs):
        dictionary = {arg: value for arg, value in zip(func.__code__.co_varnames, args)}
        dictionary.update({key: value for key, value in kwargs.items()})
        list_of_dict.append(dictionary)
        return list_of_dict

    return wrapper


def in_json(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        with open(f'{func.__name__}.json', 'w') as data:
            json.dump(result, data, indent=2)
        return result

    return wrapper


@in_json
@func_json
def task3(a, b, c, e='22', m='11'):
    return True


def param(count: int):
    def deco(func):
        my_list = []

        def wrapper(*args, **kwargs):
            for i in range(count):
                result = func(*args, **kwargs)
                my_list.append(result)
            return my_list

        return wrapper

    return deco


@param(3)
def sum_(a, b):
    return a + b


"""Объедините функции из прошлых задач.
Функцию угадайку задекорируйте:
○ декораторами для сохранения параметров,
○ декоратором контроля значений и
○ декоратором для многократного запуска.
Выберите верный порядок декораторов.
"""

print(sum_(2, 4))

print(task3(1, 2, 3, m=12))
print(task3(6, 1, 3, e=100))
print(sum_(3, 4))
