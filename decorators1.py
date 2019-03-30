# Decorators

from datetime import datetime


def timeit(func):
    def wrapper():
        start = datetime.now()
        result = func()
        print(datetime.now() - start)
        return result

    return wrapper


@timeit
def get_positive():
    list_ = []
    for i in range(10 ** 4):
        if i % 2 == 0:
            list_.append(i)
    return list_



@timeit
def get_positive_gen():
    return [x for x in range(10 ** 4) if x % 2 == 0]


# l1 = timeit(get_positive)()
l1 = get_positive()
l2 = get_positive_gen()

# print(l1)
# print(l2)
