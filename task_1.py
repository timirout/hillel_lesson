from datetime import datetime
from functools import wraps


def main_deco(max_len=23):
    def deco(func):
        # @wraps(func)
        def wrapper(*args, **kwargs):  # *args -> (1, 2, 3, 4, 5)  **kwargs -> {a: 2, b: 3}
            start = datetime.now()
            result = func(*args, **kwargs)
            end = datetime.now() - start
            print(max_len)
            print(end)
        return wrapper
    return deco


@main_deco(max_len=15)
def some_func(counter):
    """
    Some Function
    :param counter:
    :return:
    """
    lis = list()
    for i in range(counter):
        lis.append(i)


print(help(some_func))
# some_func(10000000)
