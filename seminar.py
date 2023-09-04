from functools import wraps
import json


def our_cash(func: callable):
    try:
        with open(f'{func.__name__}.json', 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        arg = str(args) + str(kwargs)
        data_res = data.get(arg)
        if data_res:
            return data_res
        result = func(*args, **kwargs)
        data.update({arg: result})
        with open(f'{func.__name__}.json', 'w') as f:
            json.dump(data, f, indent=4)
        return result

    return wrapper


def param(count: int):
    def decor(func):
        my_list = []

        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(count):
                result = func(*args, **kwargs)
                my_list.append(result)
            return my_list

        return wrapper

    return decor


@our_cash
@param(5)
def sum_(a, b):
    return a + b


print(sum_(4, 12))
