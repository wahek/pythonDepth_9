"""Нахождение корней квадратного уравнения
Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл."""
import json
import math
import random
import csv


def gen_csv():
    dict_list = []

    def wrapper(count: int = random.randint(100, 1001)):
        if not 100 < count < 1000:
            count = random.randint(100, 1001)
        for _ in range(count):
            dict_list.append({'a': random.randint(1, 9),
                              'b': random.randint(-16, 17),
                              'c': random.randint(-64, 65)})
        with open('csv.csv', 'w') as data:
            dict_write = csv.DictWriter(data, fieldnames=['a', 'b', 'c'], lineterminator='\n')
            dict_write.writeheader()
            dict_write.writerows(dict_list)
        return

    return wrapper


def root(filename: str):
    def deco(func):
        list_dict = []

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'r') as data:
                res = csv.DictReader(data, fieldnames=['a', 'b', 'c'])
                res.__next__()
                for item in res:
                    discr = int(item['b']) ** 2 - 4 * int(item['a']) * int(item['c'])
                    if discr > 0:
                        x1 = (-int(item['b']) + math.sqrt(discr)) / (2 * int(item['a']))
                        x2 = (-int(item['b']) - math.sqrt(discr)) / (2 * int(item['a']))
                        list_dict.append({item.values(): (round(x1, 2), round(x2, 2))})
                    elif discr == 0:
                        x = -int(item['b']) / (2 * int(item['a']))
                        list_dict.append({item.values(): round(x, 2)})
                    else:
                        list_dict.append({item.values(): None})
            return list_dict

        return wrapper

    return deco


def in_json(filename):
    def deco(func):
        new_dict = func
        print(new_dict)

        def wrapper(*args, **kwargs):
            print(new_dict)
            with open(filename, 'w') as data:
                json.dump(args, data, indent=2)

            return

        return wrapper

    return deco


gen_csv()(500)


@in_json('json.json')
@root('csv.csv')
def gen(count: int):
    c = count
    return c

# @in_json('csv.csv')
# def a(func):
#     print(func)
