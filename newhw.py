import csv
import json
import math


def csv_to_list(filename):
    def deco(func):
        with open(filename, 'r') as data:
            res = csv.DictReader(data, fieldnames=['a', 'b', 'c'])
            res.__next__()
            res = list(res)

        def wrapper(*args):
            f = func(res)
            return f

        return wrapper

    return deco


def in_json(filename):
    def deco(func):

        def wrapper(*args):
            a = list(func(args))
            print(a)
            with open(filename, 'w') as data:
                print(type(a))
                json.dump(a, data, indent=2)

            return

        return wrapper

    return deco


@in_json('json.json')
@csv_to_list('csv.csv')
def root(list_of_dict: list):
    list_dict = []
    for item in list_of_dict:
        discr = int(item['b']) ** 2 - 4 * int(item['a']) * int(item['c'])
        if discr > 0:
            x1 = (-int(item['b']) + math.sqrt(discr)) / (2 * int(item['a']))
            x2 = (-int(item['b']) - math.sqrt(discr)) / (2 * int(item['a']))
            list_dict.append({str(item.values()): (round(x1, 2), round(x2, 2))})
        elif discr == 0:
            x = -int(item['b']) / (2 * int(item['a']))
            list_dict.append({str(item.values()): round(x, 2)})
        else:
            list_dict.append({str(item.values()): None})
    return list_dict


root()
