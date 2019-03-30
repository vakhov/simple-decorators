# Decorators

from datetime import datetime


def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result

    return wrapper


@timeit
def get_positive(n):
    list_ = []
    for i in range(n):
        if i % 2 == 0:
            list_.append(i)
    return list_


@timeit
def get_positive_gen(n):
    return [x for x in range(n) if x % 2 == 0]


l1 = get_positive(10_000)
l2 = get_positive_gen(10_000)
